# 📷 QR 코드 실시간 인식 및 URL 열기 (`qr_scan.py`)

## 📌 실습 목표
- OpenCV와 pyzbar를 사용하여 웹캠으로 실시간 QR 코드를 인식하고,
- 인식된 QR 코드가 URL일 경우, **사용자가 Enter 키를 눌렀을 때** 해당 URL을 웹 브라우저로 열 수 있도록 구현합니다.

---

## 🛠️ 사용 기술
- `OpenCV`: 실시간 웹캠 영상 처리
- `pyzbar`: QR 코드 디코딩
- `webbrowser`: URL 자동 실행
- `cv2.waitKey`: 키보드 입력 감지 (`Enter` 키)

---

## 📈 커밋 기반 개발 흐름

| 커밋 메시지 | 주요 내용 |
|-------------|-----------|
| `qr테스트 코드 작성` | pyzbar와 OpenCV를 이용한 기본 QR 인식 코드 작성 |
| `디코드 추가` | QR 코드에서 텍스트 추출 기능 추가 |
| `선 테두리 추가` | QR 코드 테두리 시각화 기능 추가 |
| `중간 수정` | 코드 구조 개선 및 중간 테스트 |
| `qr코드 인식 시 url열기` | 인식된 QR 코드가 URL일 경우 자동으로 웹브라우저로 열기 |
| `qr코드 실시간 인식중일 때 엔터 키 클릭 시 url열기` | 실시간 인식 중 Enter 키를 눌러야만 URL이 열리도록 개선 (사용자 제어 추가) |

---

## 💡 사용 방법

1. 웹캠이 연결된 상태에서 Python 스크립트를 실행합니다.
2. 화면에 QR 코드를 비추면 자동으로 인식됩니다.
3. 인식된 내용이 URL이라면, `Enter 키`를 눌러 브라우저에서 열 수 있습니다.

-----------------------------------------------------------------------------------------------------------------------------------------

# 📁 File Browser 설치 및 사용 (Windows + PowerShell)

## 📌 목표
- Windows에서 PowerShell을 통해 **File Browser**를 설치하고,
- 로컬 폴더를 웹 브라우저에서 탐색할 수 있는 파일 서버를 실행하는 법을 익혔습니다.

---

## 🔧 설치 방법

### 1. PowerShell 관리자 권한으로 실행
- 시작 메뉴에서 "PowerShell" 검색 후 **우클릭 → 관리자 권한으로 실행**

### 2. TLS 설정 (SSL 오류 방지)
```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
3. 설치 스크립트 실행
powershell
복사
편집
iwr -useb https://raw.githubusercontent.com/filebrowser/get/master/get.ps1 | iex
🔒 Program Files에 접근 거부 오류가 발생할 경우, 반드시 관리자 권한으로 PowerShell을 실행해야 합니다.

🚀 사용 방법
기본 실행
powershell
복사
편집
filebrowser -r .
-r . 옵션은 현재 디렉토리를 루트로 지정

웹 브라우저에서 접속
arduino
복사
편집
http://localhost:8080
🔑 기본 로그인 정보
항목	값
사용자명	admin
비밀번호	admin

최초 로그인 후 꼭 비밀번호를 변경하세요!

⚙️ 유용한 실행 옵션
powershell
복사
편집
# 특정 폴더를 루트로 지정
filebrowser -r "C:\Users\YourName\Documents"

# 특정 포트에서 실행
filebrowser -r . --port 8888

# 설정 파일 직접 지정
filebrowser -r . --config "C:\path\to\.filebrowser.json"
📌 요약
PowerShell을 통해 간단히 설치 가능

설치 후 명령 한 줄로 로컬 폴더를 브라우저에서 탐색 가능

실습에서는 관리자 권한과 TLS 설정이 중요

-----------------------------------------------------------------------------------------------------------------------------------------

# 🎥 Camera Calibration & QR 인식 예제 정리

## 📁 프로젝트 구성

| 파일명 | 설명 |
|--------|------|
| `calibration3.py` | 카메라 캘리브레이션 수행 (체스보드 이미지 기반) |
| `camera_calibration.pkl` | 카메라 내부 파라미터 저장 (Pickle 파일) |
| `distanceDetection2.py` | 거리 측정 후 일정 거리 이내일 경우 경고 메시지 출력 |
| `photo.py` | 카메라로 사진을 촬영하여 저장 |
| `qr_scan.py` | QR코드를 실시간으로 인식하고, 인식이 끝났을 때 Enter 키 입력 시 URL 열기 |
| `qr_scan2.py` | `qr_scan.py`와 유사하며, 거리 감지를 추가하여 경고 메시지 출력 |
| `scanArucoMarker2.py` | ArUco 마커를 인식하여 ID 추출 |

---

## 📌 주요 기능 요약

### 🔧 1. 카메라 캘리브레이션 관련
- **`calibration3.py`**  
  체스보드 패턴을 사용하여 카메라 왜곡 보정 파라미터를 추정합니다.
  
- **`photo.py`**  
  실시간으로 웹캠에서 이미지를 촬영해 캘리브레이션에 사용할 수 있도록 저장합니다.

- **`camera_calibration.pkl`**  
  보정된 카메라 행렬, 왜곡 계수 등을 저장하는 파일입니다 (pkl 형식).

---

### 🧠 2. 거리 인식 & 경고 메시지
- **`distanceDetection2.py`**  
  특정 물체가 카메라와 가까워지면 경고 메시지를 출력하여 안전 거리 유지를 도와줍니다.

---

### 📷 3. QR 코드 인식
- **`qr_scan.py`**  
  실시간 QR 코드 인식 후 사용자가 Enter 키를 누르면 해당 URL을 브라우저로 엽니다.

- **`qr_scan2.py`**  
  거리 감지 기능이 포함된 QR 인식 버전으로, 가까이 접근 시 경고 메시지를 함께 출력합니다.

---

### 🎯 4. ArUco 마커 인식
- **`scanArucoMarker2.py`**  
  OpenCV의 ArUco 모듈을 사용해 마커를 인식하고, 해당 ID를 추출합니다.

---

## ✅ 학습 목표
- 카메라의 왜곡을 보정하고 정확한 거리 측정 수행
- QR 및 ArUco 마커를 실시간으로 인식
- 다양한 센서 기반 이미지 처리 기초 익히기
