import os
import json

def setFilePath(fileName):  
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    # '현재 이 코드가 적혀있는 파이썬 파일'이 위치한 폴더의 절대경로

    dbPath = os.path.join(BASE_PATH, 'db')
    # 그 절대경로에다가 db 폴더경로를 만들기
    if not os.path.exists(dbPath):
        os.makedirs(dbPath)  
    # 만약에 db폴더 경로가 없으면 새로 폴더 만들기
    return os.path.join(dbPath, fileName)

def save_data(fileName, data): 

    dbFilePath = setFilePath(fileName) 

    with open(dbFilePath, 'w', encoding= 'utf-8') as f:
        # 그 파일경로에 저장하는데 json형식으로 담아
        json.dump(data, f, ensure_ascii = False, indent = 4)   

def load_data(fileName, data): 

    dbFile = setFilePath(fileName) 
       
    if not os.path.exists(dbFile):  
        save_data(fileName, data) 
        # 만약에 db폴더 내 파일이 없으면 , 
        # "save_data를 써서 빈 깡통 파일부터 먼저 하나 만들어 open()이 실행되면
        #  깡통파일이 만들어지는 원리를 응용 -> json형식의 빈 파일을 만들기 위해 save() 실행
        return data

    with open(dbFile, 'r', encoding='utf-8') as f:
        return json.load(f)
    

 