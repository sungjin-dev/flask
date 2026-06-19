import uuid

def menuResister(menudict):

    mId = str(uuid.uuid4())
    mName = input('추가할 메뉴를 입력: ')
    try:
        mPrice = int(input('추가할 메뉴 가격: '))
    except ValueError:
        print('가격은 숫자만 입력해주세요')
        return 
    mTag = input('추가할 메뉴의 카테고리를 입력(주류 or 안주): ')

    menuItems = {
        'mId': mId,
        'mName': mName,
        'mPrice': mPrice,
        'mTag':mTag,
    } 

    menudict[mId] = menuItems
 
    print('메뉴 등록이 완료되었습니다.')