def calculate(*args,**kwargs):
    args_list = list(args)
    di = {}
    
    if not args:
        return
    
    
    for k in kwargs:
        if k not in ('avg','sum','max','min'):
            return 
    
    if not kwargs:
        return
        
    if 'avg' in kwargs and kwargs['avg'] == True:
        max= 0
        for a in args_list:
            max += a
        avg = max / len(args_list)
        di["avg"] = avg
        
    
    if 'sum' in kwargs and kwargs['sum'] == True:
        sum = 0
        for a in args:
            sum += a
        di['sum'] = sum
        
    
    if 'max' in kwargs and kwargs['max'] == True:
        max = 0
        for a in args_list:
            if a >= max:
                max = a
        di['max'] = max
        
    
    if 'min' in kwargs and kwargs['min'] == True:
        min = args_list[0]
        for a in args_list:
            if min >= a:
                min = a
        di['min'] = min
    
    return di
    
        

print(calculate(10,20,30,avg=True))
print(calculate(1,2,3, sum = True, max= True))
print(calculate(100,50,200, min =True, max = True, avg =True))
print(calculate(avg= True))
print(calculate(1,2,3))
print(calculate(1,2,3,totol=True))