# 데이터 개수, 질의 개수 
d_n , n = map(int,input().split())
# 구간 합 구할 대상 배열
li = list(map(int,input().split()))
s = []
# 구간 합 리스트 만들기
for _ in range(d_n):
    s.append(0)

s[0] = li[0]
s[1] = s[0] + li[1]
s[2] = s[1] + li[2]
s[3] = s[2] + li[3]
s[4] = s[3] + li[4]




# for d_n_i in range(d_n):
#     s[d_n_i+1] = s[d_n_i] + li[d_n_i+1]     
#     if d_n - 2 == d_n_i:
#         break
 
    
# 구간 설정
for _ in range(n):
    s_n , e_n = map(int,input().split())
    if s_n == 1:
        print(s[e_n-1])
    
    else:
        print(s[e_n-1]-s[s_n-2])