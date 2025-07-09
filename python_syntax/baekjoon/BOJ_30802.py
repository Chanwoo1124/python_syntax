def t_n(x,y):
    if x % y == 0:
        result = x / y 
    else:
        result = int(x / y + 1)
    return result
      
h = int(input())
s,m,l,xl,xxl,xxxl = map(int,input().split())
t,p = map(int,input().split())

# 묶음별로 비교해서 개수 구하기, 볼펜은 몇개 더사야하는지 구하기
result = 0
result += t_n(s,t)
result += t_n(m,t)
result += t_n(l,t)
result += t_n(xl,t)
result += t_n(xxl,t)
result += t_n(xxxl,t)
print(int(result))



r = s + m + l +  xl + xxl + xxxl
p_n ,p_nn = divmod(r,p)
print(p_n,p_nn)