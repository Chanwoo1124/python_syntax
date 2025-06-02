total = int(input())
num = int(input())
total_m = 0 
for u in range(num):
    m,n = map(int,input().split())
    result = m * n
    total_m += result
if total == total_m:
    print("Yes")
else:
    print("No")