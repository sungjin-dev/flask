from menu import menu_service
from customer import customer_service
from order import order_service
from boss import boss_service
from sales import sales_service
import config as root_config
import session

def main():

    mService = menu_service.menuService()

    oService = order_service.OrderService(mService.menudict)

    cService = customer_service.customerService()

    bService = boss_service.Management()

    sService = sales_service.SaleService(mService.menudict, oService.orders)

    flag = True

    while flag:

        try:
            selectedNum = int(input('1.menu 2.order 3.customer 4.coupon 5.sale 99.system-out : '))
        except ValueError:
            print('숫자만 입력해주세요.')
            continue

        if selectedNum == root_config.MENU:

            bId = session.getloginedboss()
            
            if not bId:  
                print('관리자만 접근 가능합니다.')
                
                continue 

            print(f'{bId} 관리자님 환영합니다.')
          

            mService.run()

        elif selectedNum == root_config.ORDER:
            oService.run()

        elif selectedNum == root_config.CUSTOMER:
            cService.run()

        elif selectedNum == root_config.MANAGER:
            bService.run()

        elif selectedNum == root_config.SALES:
            sService.run()

        elif selectedNum == root_config.SYSTEM_OUT:
            flag = False

if __name__ == "__main__":
    main()

