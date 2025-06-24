a = list(input())
b= list("abcdefghijklmnopqrstuvwxyz")
for q in range(len(b)):
    if b[q] in a:
        print(a.index(b[q]),end=" ")
    else:
        print("-1",end=" ")
