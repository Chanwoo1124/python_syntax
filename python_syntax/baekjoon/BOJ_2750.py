t = int(input())
l = []

for _ in range(t):
    l.append(int(input()))

for l_v in range(len(l)):
    for l_vv in range(l_v+1,len(l)):
        if  l[l_v]> l[l_vv]:
            n = l[l_v]
            l[l_v] = l[l_vv]
            l[l_vv] = n

for i in l:
    print(i)        