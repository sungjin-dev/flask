import session 

def sign_in(customerdict):

        cId = input('고객 ID 입력:  ')
        cPw = input('고객 PW 입력:  ')
     
        if cId in customerdict and customerdict[cId]['cPw'] == cPw:
            print('로그인 성공')
            session.setloginedcustomer(cId)

        else : 
            print('로그인에 실패했습니다.')
            return
        