#일급 시민이 될려면 ->
# 1. 값을 변수에 저장
# 2. 함수에 매개변수로 전달
# 3. 함수의 반환 값




def bar(msg):
    print(msg)
    
foo = bar 

def foo(my_func,msg):
    my_func(msg)
    
    
foo(bar,"hello")
