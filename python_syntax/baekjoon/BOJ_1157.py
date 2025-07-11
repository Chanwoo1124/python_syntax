tango = input()
tango = tango.upper()

dit = {}
max = 0

for t in tango:
    if t not in dit:
        dit[t] = 1
    else:
        dit[t] += 1

for k in dit:
    if dit[k] > max:
        max = dit[k]

count = 0
result = 0
for k in dit:
    if dit[k] == max:
        count += 1
        result = k  

if count == 1:
    print(result)
else:
    print('?')