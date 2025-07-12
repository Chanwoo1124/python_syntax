n,m = map(int,input().split())
l = list(map(int,input().split()))

li = []

for l_v in range(len(l)):
    for l_i in range(l_v+1,len(l)):
        for l_i_i in range(l_i+1,len(l)):
            li.append(l[l_v]+l[l_i]+l[l_i_i])

num = 0
for val in li:
    if num < val <= m:
        num = val
    
print(num)

        