def add_numbers(*args,**kwargs):
    value =list(args)
    
    for k in kwargs:
        if k not in ('abs','only_even','unique'):
            print("None")
            return
    
    if 'abs' in kwargs and kwargs['abs'] == True:
        for i,v in enumerate(value):
            if v < 0:
                value[i] = -v
            
    
    if 'only_even' in kwargs and kwargs['only_even'] == True:
        li = []
        for v in value:
            
            if v % 2 == 0:
                li.append(v)
            value = li
                
    
    if 'unique' in kwargs and kwargs['unique'] == True:
        li  = []
        for v in args:
            if v not in li:
                li.append(v)
            value = li
    
    total = 0 
    for v in value:
        total += v
    
    
    print(f"출력: 합계는 {total}입니다.")
    
add_numbers(1,2,2,3,3,4,unique = True )