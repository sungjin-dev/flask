import session
from util import time

def orderRegister(menudict, orders):

    cId = session.getloginedcustomer()

    if not cId:
        print('로그인 부터 해주세요.')
        return

    while True:

        selectedNum = int(input('1. 주문하기 0. 종료'))

        if selectedNum == 0:
            print('주문을 종료합니다.')
            return 

        elif selectedNum == 1:

            availableMenus = []

            for item in menudict.values():

                print(f"메뉴명: {item['mName']}, 가격: {item['mPrice']}")

                availableMenus.append(item['mName'])

            oName = input('주문하고 싶은 음식를 입력하세요.')

            if oName not in availableMenus:
                print('없는 메뉴거나 오타입니다.')
                continue
 
            try:
                oCount = int(input('수량을 숫자로 입력하세요: '))
            except ValueError:
                print('수량은 반드시 숫자로 입력해야 합니다')
                continue

            if cId not in orders:
                orders[cId] = {}
        
            orderCheck = {
                oName:{
                'oCount': oCount,
                'regDate': time.getCurrentDateTime()    
                }     
            }
            
            orders[cId].update(orderCheck)

            print(f'[{oName} {oCount}개] 주문이 완료되었습니다')

        else: 
            print('오타거나 잘못 누르셨습니다.')



        