def contanins(arg_lisg,arg_target):
    for v in arg_lisg:
        if v == arg_target:
            return True
    return False
            

print(contanins([1,2,3,4], 3))

print(contanins([1,2,3,4], 8))