a = int(input())
b = int(input())
c = int(input())

c = str(a * b* c)
li = [0,0,0,0,0,0,0,0,0,0]

for c_v in c:
    c_v = int(c_v)
    li[c_v] += 1

for i in li:
    print(i)
