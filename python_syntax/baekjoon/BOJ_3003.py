q = [1,1,2,2,2,8]

m = list((map(int,input().split())))

ne = []

for n in range(len(q)):
    if q[n] == m[n]:
        ne.append(0)
    else:
        ne.append(q[n]-m[n])

for re in ne:
    print(re,end=" ")