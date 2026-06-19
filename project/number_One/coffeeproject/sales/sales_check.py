def totalSales(sales):

    total_revenue = 0
    
    total_revenue = sum(value['tPay'] for value in sales.values())
        
    print(f'현재까지의 총 매출액은 {total_revenue}원 입니다.')
    return total_revenue
    