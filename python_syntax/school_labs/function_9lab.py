def student_score(name,**scores):
    print(f"{name}의 성적:\n- math: {scores['math']}점\n- english: {scores['english']}점\n- science: {scores['science']}점")
    score_sum = scores['math'] +scores['english']+scores['science'] 
    print(f"총점: {score_sum}점")   


student_score("민수", math = 90, english = 85 , science = 88)