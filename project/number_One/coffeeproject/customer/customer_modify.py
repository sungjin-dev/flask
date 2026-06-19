import session

def modify(customerdict):

    cId = session.getloginedcustomer()
    if not cId:
        print('로그인부터 해주세요.')
        return

    if cId not in customerdict:
        print('존재하지 않는 회원 정보입니다.')
        return

    cPw = input('변경하고 싶은 PW를 입력하세요: ')
    cPhone = input('변경하고 싶은 PHONE을 입력하세요: ')

    customerdict[cId]['cPw'] = cPw
    customerdict[cId]['cPhone'] = cPhone
   
    print('성공적으로 변경 처리되었습니다.')