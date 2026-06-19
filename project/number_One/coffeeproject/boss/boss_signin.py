import session 

def bossSignIn(bossdict):

        bId = input('관리자 ID 입력:  ')
        bPw = input('관리자 PW 입력:  ')
     
        if bId in bossdict and bossdict[bId]['bPw'] == bPw:
            print('관리자 로그인 성공')
            session.setloginedboss(bId) 

        else : 
            print('관리자 로그인에 실패했습니다.')
            return
        