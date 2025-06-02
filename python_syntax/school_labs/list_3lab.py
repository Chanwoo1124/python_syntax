li = []

while True:
    print("작업을 선택하세요:\n1: 추가 (create)\n2. 조회 (Read)\n3: 수정 (Update)\n4: 삭제(Delete)\n5: 종료 (Exit)")
    input_value = int(input("입력:"))
    if input_value == 1:
        li.append(int(input("추가할 값을 입력하세요:")))
        print("추가 완료.")
    
    elif input_value == 2:
        print("현재 리스트 내용")
        for i ,value in enumerate(li):
            print(f"{i}: {value}")

    elif input_value == 3:
        index = int(input("수정할 인덱스를 입력하세요"))
        if 0 <= index < len(li):
            index_value = int(input("새로운 값을 입력하세요:"))
            li[index] = index_value
            print("수정 완료.")
        else:
            print("유효하지 않은 인덱스입니다.")
    elif input_value == 4:
        index = int(input("삭제할 인덱스를 입력하세요"))
        if 0 <= index < len(li):
            li.pop(index)
            print("삭제 완료.")
        else:
            print("유효하지 않은 인덱스입니다.")

    elif input_value == 5:
            print("프로그램을 종료합니다.")
            break
    
    else:
        print("올바른 번호를 입력하세요")
        print()








