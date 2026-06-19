import session

def delete(customerdict):
      
    if session.getloginedcustomer() == '':
        print('로그인부터 해주세요.')
        return
    
    cId = session.getloginedcustomer()

    if cId in customerdict:
        del customerdict[cId] 

    print('성공적으로 탈퇴 처리되었습니다.')
   




