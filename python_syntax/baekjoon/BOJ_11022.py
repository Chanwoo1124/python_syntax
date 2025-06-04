import sys
test = int(input(""))
num = 1
for t in range(test):
    a,b = map(int,sys.stdin.readline().split())
    print(f"Case #{num}: {a} + {b} = {a+b}")
    num += 1