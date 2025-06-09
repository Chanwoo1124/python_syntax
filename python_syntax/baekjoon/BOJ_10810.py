basket = []
basket_num, ball = map(int,input().split())

for _ in range(basket_num):
    basket.append(0)

for _ in range(ball):
    sta_index,end_index,ball_num = map(int,input().split())
    for index in range(sta_index-1,end_index):
        basket[index] = ball_num

for value in basket:
    print(value,end=" ")