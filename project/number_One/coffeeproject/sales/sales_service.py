import database
from sales import config as sales_config
from sales import sales_check
from sales import sales_counted

class SaleService:
    def __init__(self, data1, data2):
        self.filename = "sales.json"
        self.menudict = data1
        self.orders = data2
        self.sales = {}

        self.sales = database.load_data(self.filename, self.sales)  

    def Payment(self):
        sales_counted.salesCount(self.menudict, self.orders, self.sales)
        database.save_data(self.filename, self.sales)
        
    def salesNow(self):
        sales_check.totalSales(self.sales)  
        database.save_data(self.filename, self.orders)

    def run(self):

        flag = True
        while flag:
            try:
                selectedNum = int(input('1. 주문 계산, 2. 매출 현황, 99. 종료 : '))
            except ValueError:
                print('숫자만 입력해주세요.')
                continue
            
            if selectedNum == sales_config.INPUT_ORDER:
               self.Payment() 
            elif selectedNum == sales_config.ORDER_STATUS:
                self.salesNow()
            elif selectedNum == sales_config.SYSTEM_OUT:
                flag = False
            else:
                print('오타거나 없는 메뉴입니다. 다시 입력해주세요.')
            
if __name__=="__main__":
    pass
