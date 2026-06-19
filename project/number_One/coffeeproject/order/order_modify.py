def modify(orders):
    
    if not orders:
        print('등록된 주문이 없습니다.')
        return 
    
    print(f'상품ID LIST: {orders}')
    
    selectedId = input('변경할 주문을 선택하세요.') 

    if selectedId not in orders:
        print('오타거나 없는 주문입니다.')
        return
    else: 
        mCount = input('주문 회수를 수정해주세요')

        orders[selectedId]['mCount'] = mCount

