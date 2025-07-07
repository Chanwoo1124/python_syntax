num= int(input())

for s in range(1,num+1):
    print(" "* (num-s) +"*"*(s*2-1))
    
for s in range(num-1,0,-1):
    print(" " *(num-s)+"*"*(s*2-1))