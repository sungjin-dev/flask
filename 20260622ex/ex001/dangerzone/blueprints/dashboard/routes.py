from flask import (
    Blueprint, 
    Response, 
    render_template,
    session,
    redirect,
    jsonify,
    request)

from ai.camera_manager import get_frame
from utils.json_manager import load_intrusion_logs

import cv2
import time
# 1단계에서 열심히 그려낸 이미지를 사용자의 웹 브라우저로 쏴주는 '송신탑' 역할
dashboard_bp = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/dashboard'
)

@dashboard_bp.route('/')
def dashboard():
    
    if session.get('signinedMemberId') is None:
        return redirect('/member/signin_form')
    
    return render_template('dashboard/dashboard.html')

@dashboard_bp.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype = 'multipart/x-mixed-replace; boundary=frame'  # MJPEG (Motion JPEG) 스트리밍의 실제 HTTP 표준 규격입니다.
    )

def generate_frames():
    
    while True:

        frame = get_frame()

        if frame is None:
            time.sleep(0.1)  # 무한 루프 안에서 실패(예외) 상황을 처리할 때는 반드시 CPU가 숨 쉴 틈(time.sleep)을 주어야 한다
            continue

        ret, buffer = cv2.imencode('.jpg', frame)  # 이미지 압축

        if not ret:          # ret는 'Return'(반환값) 또는 'Result'(결과)의 줄임말
            time.sleep(0.1)  
            continue

        frame_bytes = buffer.tobytes()

        yield (              # yield를 쓰면 "잠깐, 연결 끊지 말고 기다려 하면서 사진 조각들을 0.03초마다 무한으로 발사합니다.
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame_bytes +
            b'\r\n'
        )

        time.sleep(0.03)

@dashboard_bp.route('/get_logs')
def get_logs():
    logs = load_intrusion_logs()
    logs.reverse() # 최신순으로 뒤집기
    
    # 1. 브라우저(달력)에서 보낸 날짜를 확인합니다.
    selected_date = request.args.get('date')
    
    # 2. 날짜를 선택했다면, 그 날짜(예: 2026-06-22)가 포함된 로그만 남깁니다.
    if selected_date:
        filtered_logs = [log for log in logs if selected_date in log['time']]
    else:
        filtered_logs = logs # 선택 안 했으면 전체 보기
        
    # 3. 데이터가 너무 많으면 짤리니까 15개까지만 보냅니다.
    recent_logs = filtered_logs[:15]
    
    return jsonify(recent_logs)




# view 가 change되는 것이 아니라 이미지 데이터만 전송하면 된다 
# 이미 뷰가 있기 떄문에 render_template로 뷰를 생성할 필요가 없이
# 사진 -> 바디 헤더값으로 보내는 코드가 yield안 쪽 코드

# Contour (컨투어)는 사전적으로 '윤곽', '외곽선', '등고선



