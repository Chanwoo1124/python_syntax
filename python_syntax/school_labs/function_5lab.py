def is_even(arg_num):
    result = ""
    if arg_num % 2 == 0:
        result = "True"
    else:
        result = "False"
    
    return result

print(is_even(4))
print(is_even(5))