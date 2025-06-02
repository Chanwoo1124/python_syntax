# def plot(*args):
#     last_index = len(args) - 1
#     msg = "[ "
    
#     for idx,val in enumerate(args):
#         msg += str(val) + "," if idx != last_index else str(val)
#     msg += " ]"
    
#     print(msg)
    
# plot(1)
# plot(1,2)
# plot(1,2,"hello")

def prt_element(a,b,c,e = 1000,*d):
    print(a,b,c,d,e)
    
prt_element(1,2,3)

# 이렇게 사용하지마라 이유 생각해보기