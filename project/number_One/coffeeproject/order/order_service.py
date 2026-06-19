import database
from order import config as order_config
from order import order_register
from order import order_check
from order import order_modify

class OrderService:
    def __init__(self, data):
        self.filename = "orders.json"
        self.menudict = data
        self.orders = {}

        self.orders = database.load_data(self.filename, self.orders)  

    def orderRegister(self):
        order_register.orderRegister(self.menudict, self.orders)
        database.save_data(self.filename, self.orders)
    def orderCheck(self):
        order_check.orderCheck(self.orders)
    def orderModify(self):  
        order_modify.modify(self.orders)
        database.save_data(self.filename, self.orders)

    def run(self):

        flag = True
        while flag:
            try:
                selectedNum = int(input('1. 주문 입력, 2. 주문 현황, 3. 주문 수정, 99. 종료 : '))
            except ValueError:
                print('숫자만 입력해주세요.')
                continue
            
            if selectedNum == order_config.INPUT_ORDER:
                self.orderRegister()  
            elif selectedNum == order_config.ORDER_STATUS:
                self.orderCheck()
            elif selectedNum == order_config.ORDER_MODIFY:
                self.orderModify()
            elif selectedNum == order_config.SYSTEM_OUT:
                flag = False
            else:
                print('오타거나 없는 메뉴입니다. 다시 입력해주세요.')
            
if __name__=="__main__":
    OrderService({}).run()
