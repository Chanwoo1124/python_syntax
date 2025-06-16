def contanins(arg_lisg,arg_target):
    result = ""
    for n in arg_lisg:
        if n == arg_target:
            result = "True"
            break
        else:
            result = "False"
    return result

print(contanins([1,2,3,4], 3))

print(contanins([1,2,3,4], 8))