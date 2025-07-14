N = int(input())

for n in range(1,N):
    n_n = list(str(n))
    l_n = list(map(int,n_n))
    if N == n + sum(l_n):
        print(n)
        break
else :
    print(0)
