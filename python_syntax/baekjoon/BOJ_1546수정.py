# 성적 개수 입력
n = int(input())

# 성적 입력 (리스트)
grades = list(map(int,input().split()))

# 리스트안에 맥스 값을 모든 수에 곱하기
max = max(grades)
sum = 0
for n_i in range(n):
    sum += grades[n_i] / max *100
    

# 새로운 평균 값 출력
print(sum/n)