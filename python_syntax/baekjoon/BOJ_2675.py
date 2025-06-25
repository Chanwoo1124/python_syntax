test = int(input())


while test:
    num_1,str_1 = input().split()  
    
    for s in str_1:
        print(s * int(num_1), end="")
    print()
    test -= 1