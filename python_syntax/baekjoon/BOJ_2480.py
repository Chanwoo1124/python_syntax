a,b,c = map(int,input().split())
max = 0
if a == b== c:
    print(f"{10000+a * 1000}")

elif a == b :
    print(f"{1000+a*100}")
elif a == c:
    print(f"{1000+a*100}")
elif b == c:
    print(f"{1000+b*100}")
else:
    max = a
    if b > a:
        max = b
    if c > max:
        max = c
    print(max * 100)