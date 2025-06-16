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

# def prt_element(a,b,c,e = 1000,*d):
#     print(a,b,c,d,e)
    
# prt_element(1,2,3)

# 이렇게 사용하지마라 이유 생각해보기

# def bar (a,b,*c):
#     print(a,b)
#     print(c)
    
# foo = [val for val in range(1,10)]

# bar(*foo)

# def bar(a,*b, c = 10, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(kwargs)
    
# foo = [val for val in range(1,10)]
# pos = {'d': 10, 'e': 20 , 'f': 30}

# bar(*foo,**pos)

# dict 언패킹 할려면 ** 으로 해야하고 언패킹을 하면 키워드 인자값으로 변함 a = 10 , e = 20 , f = 30

bar = [10,20,30]

print(bar)
def foo(arg_list):
    arg_list[0] = 100
    
foo(bar)

print(bar)   
""" bar 라는 원본의 값이 바뀜(메모리주소 값이 넘어가면서 원본의 값을 건들임)""" 
kin = 3

def foo(arg):
    arg = 10
    
print(kin)
""" 얘들은 값이 복사가 되서 넘어가서 원본 값을 건들이지 않음""" 