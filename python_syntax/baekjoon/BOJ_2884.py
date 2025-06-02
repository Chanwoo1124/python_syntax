h ,m =map(int,input().split())
l = 0
if h == 0:
    if m < 45:
        l = m - 45
        min = 60 + l    
        print("23", min)
    else:
        print("0" ,m-45)

else:
    if m < 45:
        h -= 1
        l = m - 45
        min = 60 + l
        print(h , min)
    else:
        m -= 45
        print(h, m)