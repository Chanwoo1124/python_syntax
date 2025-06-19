def calculate_average(*args):
    n = len(args)
    s = 0
    for a in args:
        s += a
    avg = s / n      
    
    return n , s, avg


n,s,avg = (calculate_average(70,80,90,100,200))

print(n,s,avg)