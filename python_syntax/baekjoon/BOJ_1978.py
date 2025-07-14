# 주어진 수 입력
num = int(input())

# 주어진 수 만큼 입력
l = list(map(int,input().split()))

# 소수 찾기
for l_v in l:
    if l_v == 1:
        num -= 1
    else:
        for n in range(2,l_v):
            if l_v % n == 0:
                num -= 1
                break
print(num)