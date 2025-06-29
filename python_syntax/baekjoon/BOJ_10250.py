t = int(input())

for _ in range(t):
    H,W,N = map(int,input().split())
    
    if N % H == 0:
        fl = H
        ro = N//H
    
    else:
        fl = N % H
        ro = N // H+1
    
    
    print(fl*100+ro)