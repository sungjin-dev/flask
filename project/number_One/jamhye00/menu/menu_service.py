from menu import config as menu_config
import os
import json
import session

class MenuService:

    def __init__(self):
        self.cafeMenus = {}
        self.init_database()

    def run(self):

        flag = True
        while flag:
            menuNum = int(input('1.등록 2.조회 3.수정 4.삭제 0.뒤로가기'))
            
            if menuNum == menu_config.MENU_CREATE:
                self.menu_create()
            elif menuNum == menu_config.MENU_VIEW:
                self.menu_view()
            elif menuNum == menu_config.MENU_MODIFY:
                self.menu_modify()
            elif menuNum == menu_config.MENU_DELETE:
                self.menu_delete()
            elif menuNum == menu_config.MENU_EXIT:
                flag = False

    def menu_create(self):
        id = input('id 입력: ')
        name = input('메뉴 입력: ')
        price = input('가격 입력: ')
        category = input('카테고리 입력: ')
        isAvailable = int(input('1.판매중 2.품절'))

        if isAvailable == 1:
            isAvailable = True
        elif isAvailable == 2:
            isAvailable = False

        cafeMenu = {
            'menuId': id,
            '메뉴명': name,
            '가격': price,
            '카테고리': category,
            '판매여부': '판매중' if isAvailable else '품절'
        }
        self.cafeMenus[id] = cafeMenu

        self.save_menus(self.cafeMenus)

    def menu_view(self):
        self.cafeMenus = self.load_menus()
        print(f'{self.cafeMenus}')

    def menu_modify(self):
        newName = input('메뉴 입력: ')
        newPrice = input('가격 입력: ')
        newCategory = input('카테고리 입력: ')
        newIsAvailable = int(input('1.판매중 2.품절'))

        if newIsAvailable == 1:
            newIsAvailable = True
        elif newIsAvailable == 2:
            newIsAvailable = False

        self.cafeMenus = self.load_menus()
        updateMenu = self.cafeMenus[session.getSignInedMenuId()]

        updateMenu['메뉴명'] = newName
        updateMenu['가격'] = newPrice
        updateMenu['카테고리'] = newCategory
        updateMenu['판매여부'] = '판매중' if newIsAvailable else '품절'

        self.save_menus(self.cafeMenus)
        
    def menu_delete(self):
        confirm = input('메뉴를 정말 삭제하시겠습니까? [Y] or [N]')

        if confirm == 'Y' or 'y':
            self.cafeMenus = self.load_menus()
            del self.cafeMenus[session.getSignInedMenuId()]

            self.save_menus(self.cafeMenus)
        
            session.setSignInedMenuId()
            print('메뉴가 삭제되었습니다')

    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'menus.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_menus(self.cafeMenus)
        else:
            self.cafeMenus = self.load_menus()

    def save_menus(self, cafeMenus):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(cafeMenus, f, ensure_ascii=False, indent=4)
    
    def load_menus(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    menu_service = MenuService()
    menu_service.run()