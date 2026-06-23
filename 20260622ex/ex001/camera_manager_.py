import cv2
import threading
from utils.json_manager import load_intrusion_logs, save_intrusion_logs, save_intrusion_log 
from datetime import datetime, timedelta
import os

from utils.json_manager import (
    load_intrusion_logs,
    save_intrusion_logs
)

# camera_manager 파일은 카메라 영상을 받아와서 분석하고 위험을 판단하는 '뇌' 역할

camera = None
camera_lock = threading.Lock()

ESP32_STREAM_URL = "http://192.168.137.3:81/stream"

prev_gray = None
last_intrusion_time = None


# 고정 위험구역 좌표
DANGER_X1 = 170  # 320 - 150
DANGER_Y1 = 115  # 240 - 125
DANGER_X2 = 470  # 320 + 150
DANGER_Y2 = 365


def init_camera():

    global camera

    if camera is None:
        print("camera connecting...")
        camera = cv2.VideoCapture(ESP32_STREAM_URL)
        print("camera connected")


def reconnect_camera():

    global camera

    print("camera reconnecting...")

    try:                       # 단순히 작동 안 된다고 return해서 서버를 닫는게 아니라 자동복구 시스템 
        if camera is not None:
            camera.release()
    except:
        pass

    # 💡 핵심 방어막: 무한 재시도로 인한 과부하를 막기 위해 3초간 숨을 고릅니다.
    import time
    time.sleep(3)

    camera = cv2.VideoCapture(ESP32_STREAM_URL)

    print("camera reconnected")


def get_frame():

    global camera
    global prev_gray
    global last_intrusion_time

    if camera is None:
        return None

    try:

        if not camera.isOpened():
            reconnect_camera()
            return None

        with camera_lock:  # 이건 알고 넘어가기 
            success, frame = camera.read()
# threading.Lock()을 사용해 "한 놈이 사진 뽑아갈 동안 다른 놈들은 잠깐 대기해!"라고 줄을 세운 것은 멀티스레드 서버 환경에서 필수적인 고급 기술입니다.
        if not success:
            reconnect_camera()
            return None

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (21, 21),
            0
        )

        is_intrusion = False

        if prev_gray is None:

            prev_gray = gray

        else:

            diff = cv2.absdiff(   #0.1초 전 화면과 지금 화면을 비교해서 '달라진 부분(움직임)'만 찾아냄
                prev_gray,
                gray
            )

            _, thresh = cv2.threshold(
                diff,
                25,
                255,
                cv2.THRESH_BINARY
            )

            contours, _ = cv2.findContours(   # 그 달라진 부분의 윤곽선을 따서 덩어리를 만듭니다.
                thresh,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            for contour in contours:

                if cv2.contourArea(contour) < 500:  
                    continue

                x, y, w, h = cv2.boundingRect(
                    contour
                )

                center_x = x + w // 2
                center_y = y + h // 2

                cv2.rectangle(      # 덩어리의 넓이가 500 이상이면 사람이나 큰 물체로 판단하고 초록색 네모(cv2.rectangle)를 씌웁니다.
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    frame,
                    (center_x, center_y),
                    5,
                    (255, 0, 0),
                    -1
                )

                if (
                    DANGER_X1 <= center_x <= DANGER_X2
                    and
                    DANGER_Y1 <= center_y <= DANGER_Y2
                ):
                    is_intrusion = True

            prev_gray = gray

        danger_color = (0, 0, 255)   

        if is_intrusion:
            danger_color = (0, 255, 255)   # 노란색

        cv2.rectangle(
            frame,
            (DANGER_X1, DANGER_Y1),
            (DANGER_X2, DANGER_Y2),
            danger_color,
            3
        )

        cv2.putText(
            frame,
            "DANGER ZONE",
            (DANGER_X1, DANGER_Y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            danger_color,
            2
        )

        if is_intrusion:

            cv2.putText(
                frame,
                "INTRUSION DETECTED",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            now = datetime.now()

            if (
                last_intrusion_time is None
                or
                now - last_intrusion_time >
                timedelta(seconds=5)    # 한 번 침입을 감지하고 나면 5초 동안은 다시 기록하지 않도록 쿨타임 중요! 과부하 방지
            ):

                save_intrusion_log(frame)

                last_intrusion_time = now

        return frame

    except Exception as e:

        print("camera exception:", e)

        reconnect_camera()

        return None