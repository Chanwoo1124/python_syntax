total_student=[]
for t in range(1,31):
    total_student.append(t)

for s in range(28):
    attendance_num = int(input())
    total_student.remove(attendance_num)

print(f"{total_student[0]}\n{total_student[1]}")
    