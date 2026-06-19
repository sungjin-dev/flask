import session

def signUp(bossdict):

    if session.getloginedboss() != '':
        print('이미 로그인되어있습니다.')
        return
    
    bId = input('ID를 입력하세요.')

    if bId in bossdict:
        print('이미 존재하는 ID입니다.')
        return
    
    bPw = input('PW를 입력하세요.')


    manager = {
        'bId':bId,
        'bPw':bPw 
    }
   
    bossdict[bId] = manager

    session.setloginedboss(bId)


    