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

def save_intrusion_logs(logs):
    with open(INTRUSION_LOG_FILE, "w", encoding='utf-8') as f:
        json.dump(
            logs,
            f,
            ensure_ascii=False,
            indent=4
        )

def save_snapshot(frame):
    now = datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S") + ".jpg"
    save_path = os.path.join(BASE_DIR, "static", "snapshots", filename)
    cv2.imwrite(save_path, frame)
    return f"static/snapshots/{filename}" 

def save_intrusion_log(x, y, image_path): 
    logs = load_intrusion_logs()
    logs.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Person Intrusion in Danger Zone",
        "position": {"x": x, "y": y},
        "image": image_path 
    })
    save_intrusion_logs(logs) 
    print(f"Intrusion logged at ({x}, {y})")
    