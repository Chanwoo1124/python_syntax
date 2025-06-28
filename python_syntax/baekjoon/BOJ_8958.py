n = int(input())


for _ in range(n):
    count  = 0
    total = 0
    s = input()
    for s_v in s:
        if s_v == "O":
            count += 1
            total += count
        
        else:
            count = 0
    print(total)