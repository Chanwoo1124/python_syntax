a,b,c,d,e = map(int,input().split())

l= [a,b,c,d,e]

total = 0
for i_v in l:
    total += i_v **2

print(total%10)    