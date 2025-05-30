t ,m = map(int,input().split())
r = int(input())


if m + r < 60:
    print(t,m+r)
else:
    h = m + r 
    a,b = divmod(h,60)
    if t + a >= 24:
        p =t + a - 24
        print(p,b)
    else:
        print(t+a,b)