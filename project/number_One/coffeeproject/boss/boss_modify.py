import session

def modify(bossdict):

    bId = session.getloginedboss()
    
    if not bId:
        print('로그인부터 해주세요.')
        return

    if bId not in bossdict:
        print('존재하지 않는 회원 정보입니다.')
        return

    bPw = input('변경하고 싶은 PW를 입력하세요: ')
   
    bossdict[bId]['bPw'] = bPw
  
    print('성공적으로 변경 처리되었습니다.')
  