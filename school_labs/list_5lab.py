import random

li = []
random_number = int(input("난수 개수를 입력하세요:"))
ran_num_sta = int(input("시작 범위를 입력하세요:"))
ran_num_last = int(input("시작 범위를 입력하세요:"))

count = 0

for _ in range(random_number):
    li.append(random.randint(ran_num_sta,ran_num_last))
    
set_li = set(li)

for s in set_li:
    for l in li:
        if s == l:
            count += 1
        
    
print(s)








# for l in li:
#     for i in li:
#         if l == i:
#             count += 1
       