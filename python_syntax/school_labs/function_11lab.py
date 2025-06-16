def add_numbers(*args, **kwargs):
    key = kwargs.keys()
    for k in key:
        if k not in ("abs" , "only_even" , "unique"):
            print("None")
            return
    
    if 'unique' in key:
        args = set(args)
        
    
    if 'abs' in key:
        args = list(map(abs,args))
        
        
    if 'only_even' in key:
        args = [value for value in args if value % 2 == 0]
    
    print(f"출력: 합계는 {sum(args)}입니다.")    
    
    
    
    

add_numbers(1,-2,2,-3) 
add_numbers(1,2, 2,3,3,4, unique = True)
add_numbers(1,-2,2,-3,abs =True, only_even = True)  
add_numbers(1,-2,2,-3,round = True)  
