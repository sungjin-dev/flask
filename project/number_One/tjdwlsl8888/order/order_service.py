from order import config as order_config
import json
import os
from menu import menu_service
from datetime import datetime


class OrderService:
    def __init__(self):
        self.orderMenus = {}
        self.init_database()

    def run(self):

        flag = True

        while flag:
            menuNum = int(input('1.주문하기 2.주문내역 조회 3.주문취소 0.뒤로가기'))
            if menuNum == order_config.ORDER:
                pass
            elif menuNum == order_config.ORDER_HISTORY:
                pass
            elif menuNum == order_config.ORDER_CANCLE:
                pass
            elif menuNum == order_config.SERVICE_OUT:
                flag = False

    def order_menu(self):

        selectedCustomerType = input('선택해주세요. [1.매장 회원 2.비회원]')
        
        if selectedCustomerType == 1:
            inputCustomerId = input('고객 ID입력: ')

        elif selectedCustomerType == 2:
            customerId = '비회원'   

        # cafemenus = menu_service.MenuService.load_menus()

        # orderMenu = input('주문할 메뉴의 ID 입력: ')
        # orderMenuCnt = input('수량 입력: ')
        # for key, value in cafemenus.items():
        #     print(key, value)

        # if orderMenu == cafemenus[key]:
            
            # orderMenus = {
            #     '주문번호': 1,
            #     '고객ID': 1,
            #     '주문메뉴':1,
            #     '수량':1,
            #     '총금액':1,
            #     '주문일시': datetime.now()
            # }

        

    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'orders.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_orderMenus(self.orderMenus)
        else:
            self.orderMenus = self.load_orderMenus()

    def save_orderMenus(self, orderMenus):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(orderMenus, f, ensure_ascii=False, indent=4)
    
    def load_orderMenus(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)   

if __name__ == "__main__":
    orderService = OrderService()
    orderService.run()