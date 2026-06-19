import config as root_config
from menu import menu_service

flag = True
while flag:
    selectedMenuNum = int(input('1.MENU-SERVICE 2.ORDER-SERVICE 3.CUSTOMER-SERVICE 4.COUPON-SERVICE 5.SALES-SERCVICE 0.SYSTEM-OUT '))
    if selectedMenuNum == root_config.MENU_SERVICE:
        menu_service.MenuService().run()
    elif selectedMenuNum == root_config.ORDER_SERVICE:
        pass
    elif selectedMenuNum == root_config.CUSTOMER_SERVICE:
        pass
    elif selectedMenuNum == root_config.COUPON_SERVICE:
        pass
    elif selectedMenuNum == root_config.SALES_SERCVICE:
        pass
    elif selectedMenuNum == root_config.SYSTEM_OUT:
        flag = False