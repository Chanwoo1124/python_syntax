basket = []
basket_num, num = map(int,input().split())

for b_n in range(1,basket_num+1):
    basket.append(b_n)

for _ in range(num):
    j,k = map(int,input().split())
    basket[j-1:k] = basket[j-1:k][::-1]
    
for b in basket:
    print(b, end=" ")