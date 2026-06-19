def menuModify(menudict):

    for idx, value in enumerate(menudict):
        print(f'번호: {idx+1} , 상품 ID: {value}')
 
    mId = input('변경할 메뉴 ID를 입력하세요.')

    if mId not in menudict:
        print('없는 ID입니다.')
        return

    mName = input('변경할 메뉴를 입력하세요.')
    mPrice = input('변경할 메뉴 가격을 입력하세요.')
    mTag = input('변경할 메뉴 카테고리를 입력하세요.')

    menudict[mId]['menuId'] = mId
    menudict[mId]['menuName'] = mName
    menudict[mId]['menuPrice'] = mPrice
    menudict[mId]['menuTag'] = mTag

    print('성공적으로 변경되었습니다.')