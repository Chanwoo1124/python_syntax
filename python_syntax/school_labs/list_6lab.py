bar = input("문자와 숫자가 섞인 문자열을 입력하세요:")

print(f"입력 문자열: {bar}")
num = []
for b in bar:
    if b.isdigit():
        num.append(b)
print(f"숫자 추출: {num}")

change_list = []
for s in num:
    if int(s) % 2 == 0:
        change_list.append(1)
    else:
        change_list.append(-1)

print(f"변환된 리스트(+1/-1): {change_list}")



for n in range(len(change_list)):
    for l_i in range(1,len(change_list)+1):
        if n < l_i:
            if sum(change_list[n:l_i]) == 0:
                print(f"합이 0인 연속 부분 수열 목록:{change_list[n:l_i]}")   
        

