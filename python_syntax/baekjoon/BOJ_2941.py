tango = input()
count = 0


tango = tango.replace('c=',"a")
tango = tango.replace('c-',"a")
tango = tango.replace('dz=',"a")
tango = tango.replace('d-',"a")
tango = tango.replace('lj',"a")
tango = tango.replace('nj',"a")
tango = tango.replace('s=',"a")
tango = tango.replace('z=',"a")

for t in tango:
    count += 1

print(count)