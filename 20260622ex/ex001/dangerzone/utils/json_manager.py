import json, os, cv2
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEMBER_FILE = os.path.join(BASE_DIR, "db", "members.json")
INTRUSION_LOG_FILE = os.path.join(BASE_DIR, "db", "intrusion_log.json")

def load_members():
    try:
        with open(MEMBER_FILE, encoding = 'utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_members(members):
    with open(MEMBER_FILE, "w", encoding='utf-8') as f:
        json.dump(
            members,
            f,
            ensure_ascii = False,
            indent = 4
        )

def load_intrusion_logs():
    try:
        with open(INTRUSION_LOG_FILE, encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

# 1. [추가] 실제 JSON 파일에 최종 리스트를 파일 쓰기(json.dump)하는 함수입니다.
def save_intrusion_logs(logs):
    with open(INTRUSION_LOG_FILE, "w", encoding='utf-8') as f:
        json.dump(
            logs,
            f,
            ensure_ascii=False,
            indent=4
        )

# 2. 카메라로부터 frame을 받아와 이미지로 저장하고 로그를 추가하는 함수입니다.
def save_intrusion_log(frame):
    logs = load_intrusion_logs()
    
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. 파일 이름 만들기 (예: 20260622_154030.jpg)
    filename = now.strftime("%Y%m%d_%H%M%S") + ".jpg"
    
    # 2. 컴퓨터 하드디스크에 저장할 진짜 경로 (os.path.join 사용 - 윈도우용 \)
    save_path = os.path.join(BASE_DIR, "static", "snapshots", filename)
    
    # 3. 인터넷 웹 브라우저가 읽을 경로 (무조건 문자열로 슬래시 / 사용!!!)
    web_path = f"static/snapshots/{filename}"
    
    # 4. 진짜 경로에 이미지 저장
    cv2.imwrite(save_path, frame)

    # 5. JSON 파일에는 인터넷 경로를 저장!
    logs.append({
        "time": time_str,
        "message": "Danger Zone Intrusion",
        "image": web_path  # 👈 여기를 filepath가 아니라 web_path로 바꿔주세요!
    })
    # 🔥 중요: 자기 자신이 아니라, 실제 파일 쓰기를 하는 1번 함수(save_intrusion_logs)를 호출해야 합니다!
    save_intrusion_logs(logs)
    print("intrusion log & snapshot saved")