num = []
n = set()
for q in range(10):
    num.append(int(input()))
    n.add(num[q] % 42)

print(len(n))