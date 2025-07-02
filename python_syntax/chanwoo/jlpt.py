num = list(map(int,input("숫자 넣으시오").split()))

l = [0,0,0,0]

for n in num:
    if n == 1:
        l[0] += 1
    elif n == 2:
        l[1] +=1
        
    elif n == 3:
        l[2] += 1
        
    else:
        l[3] += 1

print(l)