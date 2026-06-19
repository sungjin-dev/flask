import session

def orderCheck(orders):

    cId = session.getloginedcustomer()

    if not cId:
        print('로그인 부터 해주세요.')
        return 

    print(f'주문 현황: {orders[cId]}')
