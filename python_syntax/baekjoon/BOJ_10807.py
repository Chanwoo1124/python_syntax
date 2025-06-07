num = int(input())
value = list(map(int,input().split()))
find =int(input())



count = 0
for n in value:
    if n == find:
        count += 1
print(count)