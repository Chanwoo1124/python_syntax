num = int(input())

point =list(map(int,input().split()))


max = max(point)

for n in range(num):
    point[n] = point[n] / max * 100


print(sum(point)/num)
