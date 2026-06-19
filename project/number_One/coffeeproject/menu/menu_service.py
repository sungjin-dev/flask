from menu import config as memu_config
from menu import menu_register
from menu import menu_modify
from menu import menu_list
import database

class menuService:
    def __init__(self):
        self.filename = "menus.json"
        self.menudict = {}

        self.menudict = database.load_data(self.filename, self.menudict)

    def register(self):
        menu_register.menuResister(self.menudict)
        database.save_data(self.filename, self.menudict)
    def checkMenu(self):
        menu_list.checkMenuList(self.menudict)
    def menuModify(self):
        menu_modify.menuModify(self.menudict)
        database.save_data(self.filename, self.menudict)
    def menuDelete(self):
        database.save_data(self.filename, self.menudict)

    def run (self):
        
        flag = True

        while flag:
            try:    
                selectedNum = int(input('1. 메뉴 등록, 2. 메뉴 조회, 3.메뉴 수정, 4.메뉴 삭제, 99.종료' ))
            except ValueError:
                print('숫자만 입력해주세요.')
                continue
    
            if selectedNum == memu_config.MENUREGISTER:
                self.register()  
            elif selectedNum == memu_config.MENECHECK:
                self.checkMenu() 
            elif selectedNum == memu_config.MENUMODIFY:
                self.menuModify()
            elif selectedNum == memu_config.MENUDELETE:
                self.menuDelete()
            elif selectedNum == memu_config.SYSTEM_OUT:
                flag = False
          


