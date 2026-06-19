import session

def delete(bossdict):
      
    if session.getloginedboss() == '':
        print('로그인부터 해주세요.')
        return
    
    bId = session.getloginedboss()

    if bId in bossdict:
        del bossdict[bId] 
   
    session.setloginedboss('')
    
    print('성공적으로 탈퇴 처리되었습니다.')


