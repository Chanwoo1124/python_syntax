def calculate_average(*args):
    count = len(args)
    args_sum = sum(args)
    ave = args_sum/ len(args)
    return count ,args_sum , ave

n,s,avg = (calculate_average(70,80,90))

print(f"입력 개수:{n}\n총합: {s}\n평균:{avg}")


# n,s,avg = (calculate_average(70,80,90,100,200))

