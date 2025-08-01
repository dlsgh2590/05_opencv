import cv2
import pyzbar.pyzbar as pyzbar
import webbrowser

cap = cv2.VideoCapture(0)
opened_urls = set()

current_decoded_data = None  # 현재 인식된 QR 코드

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)

    if decoded:
        # 가장 첫 번째 QR 코드만 사용
        d = decoded[0]
        x, y, w, h = d.rect
        current_decoded_data = d.data.decode('utf-8')
        barcode_type = d.type

        text = f'{current_decoded_data} ({barcode_type})'
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, "Press ENTER to open", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    else:
        current_decoded_data = None

    cv2.imshow('camera', img)

    key = cv2.waitKey(1) & 0xFF

    # 엔터키 누르면 현재 인식된 QR 코드 열기
    if key == 13 and current_decoded_data:
        if current_decoded_data.startswith("http://") or current_decoded_data.startswith("https://"):
            if current_decoded_data not in opened_urls:
                webbrowser.open(current_decoded_data)
                opened_urls.add(current_decoded_data)
                print("열림:", current_decoded_data)
            else:
                print("이미 열렸음:", current_decoded_data)
        else:
            print("URL이 아님:", current_decoded_data)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
