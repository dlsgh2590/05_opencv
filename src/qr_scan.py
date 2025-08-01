import cv2 
import pyzbar.pyzbar as pyzbar
import webbrowser
import time  # ✅ 시간 간격 체크용

cap = cv2.VideoCapture(0)

opened_urls = set()        # 열었던 URL 저장
last_open_time = 0         # 마지막으로 URL 연 시간
open_interval = 5          # URL 열기 간격 (초)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)

    for d in decoded:
        x, y, w, h = d.rect 
        barcode_data = d.data.decode('utf-8')
        barcode_type = d.type

        text = f'{barcode_data} ({barcode_type})'
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # ✅ 조건: URL 형식이고, 열지 않았고, 일정 시간 지난 경우
        current_time = time.time()
        if (barcode_data.startswith("http://") or barcode_data.startswith("https://")):
            if barcode_data not in opened_urls and current_time - last_open_time > open_interval:
                webbrowser.open(barcode_data)
                opened_urls.add(barcode_data)
                last_open_time = current_time

    cv2.imshow('camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()