students = {}

while True:
    print("====학생 성적 관리 프로그램 ====")
    print('''1. 학생 성적 입력\n2. 학생 성적 출력\n3. 학생 성적 확인\n4. 학생 성적 삭제\n5. 종료''')
    menu = int(input("메뉴 선택 (1~5):"))
    if menu == 1:
        stu_num = int(input("학번 입력:"))
        stu_data = {}
            
        if stu_num in students:
            print("이미 등록된 학번입니다.")    
            
            
        else:    
            name = input("이름 입력:")
            kor = int(input("국어 성적 입력:"))
            eng = int(input("영어 성적 입력:"))
            math = int(input("수학 성적 입력:"))
            sum = kor + eng + math
            ave = sum / 3
            ave = round(ave,3)
            stu_data['이름'] = name
            stu_data['국어'] = kor
            stu_data['영어'] = eng
            stu_data['수학'] = math
            stu_data['합계'] = sum
            stu_data['평균'] = ave
            
            students[stu_num] = stu_data
            print(students)
            print("성적이 저장되었습니다.")
            
    elif menu == 2:
        if not students:
            print("저장된 학생 정보가 없습니다.")
            
        else:
            for s_k in students:
                for k  in students[s_k].keys():
                    print(k,end="\t",)
                print()
                for value  in students[s_k].values():    
                    print(value,end="\t")
                print()
    
    elif menu == 3:
        num = int(input("조회할 학번 입력:"))
        if num not in students:
            print("존재하지 않는 학번입니다.")
        
        else:
            print("[ 학생 정보]")
            print(f"학번: {num}")
            for k,value in students[num].items():
                print(f"{k}: {value}")
    
    elif menu == 4:
        num = int(input("삭제할 학번 입력:"))
        if num not in students:
            print("해당 학번의 학생 정보가 없습니다.")
        
        else:
            del(students[num])
            print("학생 정보가 삭제 되었습니다")
    
    elif menu == 5:
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("1~5 사이의 숫자를 선택하세요")
        
        