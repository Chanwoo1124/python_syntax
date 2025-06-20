import random 

num = []

li = []
for _ in range(20):
    num.append(random.randint(0,100))

li.append(num[0:5])
li.append(num[5:10])
li.append(num[10:15])
li.append(num[15:20])

while True:
    li_num = len(li)
    print("=== 리스트 관리 프로그램 ===")
    print("1.각 리스트 내 데이터 출력\n2.특정 리스트 출력\n3.특정 리스트 삭제\n4.프로그램 종료")
    menu = int(input("메뉴 선택:"))
    if menu == 1:
        for data in range(len(li)):
            print(f"[리스트 {data+1}]: {li[data]}")
            
    elif menu == 2:
        num = int(input(f"출력할 리스트 번호 1~{li_num}:"))
        if num not in range(1,li_num):
            print("리스트 번호가 범위를 벗어났습니다.")
            
        else:    
            print(f"[리스트 {num}]: {li[num-1]}")
        

    elif menu == 3:
        num = int(input(f"삭제할 리스트 번호(1~{li_num}):"))

        if num not in range(1,li_num):
            print("리스트 번호가 범위를 벗어났습니다.")
            
        else:    
            del li[num-1]
            print(f"리스트 {num}가 삭제되었습니다.")
    
    elif menu == 4:
        print("프로그램을 종료합니다.")