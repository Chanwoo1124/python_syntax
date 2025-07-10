n,m = map(int,input().split())
l = list(map(int,input().split()))

num = 0
list = []

for l_v in range(len(l)):
    for l_i in range(l_v+1,len(l)):
        for l_i_i in range(l_v+2,len(l)):
            list.append(l[l_v]+l[l_i]+l[l_i_i])
print(list)

for val in list:
    if num < val <= m:
        num = val
    
print(num)
        