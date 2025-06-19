def student_score(name,**scores):
    print(f"{name}의 성적:")
    sum_scores = 0
    for k, v in scores.items():
        print(f"-{k}: {v}점")
        sum_scores += v
    print(f"총점: {sum_scores}점")
        
student_score("민수", math = 90, english = 85 , science = 88)