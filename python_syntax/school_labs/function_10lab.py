def calc_price(product,price,tax=0.10):
    print(f"{product}의 최종 가격은 {price+price * tax:.0f}원입니다.")
    
    
    
    
calc_price("노트북",1000000)

    
calc_price("모니터",300000,tax =0.05)