n,m = map(int,input().split())

i = 0
if n > m:
    for n_n in range(1,n+1):
        if n % n_n == 0 and m % n_n == 0:
            i = n_n
else:
    for n_n in range(1,m+1):
        if n % n_n == 0 and m % n_n == 0:
            i = n_n
print(i)
print(int(n*m/i))

