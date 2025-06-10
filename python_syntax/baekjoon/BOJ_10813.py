basket = []
basket_num, num = map(int,input().split())

for b in range(1,basket_num+1):
    basket.append(b)

for _ in range(num):
    index_i, index_j = map(int,input().split())
    q = basket[index_i-1]
    basket[index_i-1] = basket[index_j-1]
    basket[index_j-1] = q

for v in basket:
    print(v,end=" ")