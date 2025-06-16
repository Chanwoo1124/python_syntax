def calc_price(product,price,tax=0.10):
    product_tax = int(price * tax)
    last_price = price + product_tax
    print(f"출력: {product}의 최종 가격은 {last_price}원입니다.")
    
calc_price("노트북",1000000)

    
calc_price("모니터",300000,tax =0.05)