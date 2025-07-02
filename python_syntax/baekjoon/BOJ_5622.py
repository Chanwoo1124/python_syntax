num = input()

count = 0

for n in num:
    if n in "ABC":
        count += 3
    elif n in "DEF":
        count += 4
    elif n in "GHI":
        count += 5
    elif n in "JKL":
        count += 6
    elif n in "MNO":
        count += 7
    elif n in "PQRS":
        count += 8
    elif n in "TUV":
        count += 9
    elif n in "WXYZ":
        count += 10
    
print(count)