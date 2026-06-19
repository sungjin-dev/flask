loginedcustomer = ''
loginedboss = ''

def setloginedcustomer(cId):
    global loginedcustomer
    loginedcustomer = cId

    print(f" 세션 저장 완료! 현재 접속자: {loginedcustomer}")

def getloginedcustomer(): 
    global loginedcustomer  
    print(f"조회 요청! 접속자: {loginedcustomer}")
    return loginedcustomer

def setloginedboss(bId):
    global loginedboss
    loginedboss = bId  

def getloginedboss():
    global loginedboss
    return loginedboss