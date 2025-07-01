a, b = input().split()

num_1= int(a[::-1])
num_2 =int(b[::-1])

if num_1 > num_2:
    print(num_1)
else:
    print(num_2)
