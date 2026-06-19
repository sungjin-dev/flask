import session
from util import time
import random

import session

def salesCount(menudict, orders, sales):

    cId = session.getloginedcustomer()

    if not cId:
        print('로그인부터 해주세요.')
        return
    
    if cId not in orders:
        print('주문 내역이 없습니다.')
        return
    
    totalPayment = 0

    myOrders = orders[cId]

    for menu, infos in myOrders.items():

        oCount = infos['oCount']

        mPrice = 0

        for item in menudict.values():
            if item['mName'] == menu:
                mPrice = item['mPrice']
                break   
    
        orderPayment = mPrice * oCount

        totalPayment += orderPayment

    today = time.getCurrentDate()
    random_num = random.randint(1, 9999)
    orderId = f'주문일{today}-주문번호{random_num:04d}'
        
    paypal = {
        'orderId': orderId,  
        'cId': cId,
        'tPay': totalPayment,
        'regDate': time.getCurrentDateTime() 
    }
   
    sales[orderId] = paypal

    print(f'{totalPayment}원 결제가 완료되었습니다.')

    del orders[cId]




