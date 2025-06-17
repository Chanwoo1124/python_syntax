def generate_profile(name,age,*interests,gender="미정",**metadata):
    print("[고객 프로필]")
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"성별: {gender}")
    
    print("관심사:",end=" ")
    for v in range(len(interests)):
        print(interests[v],end="")
        if len(interests)-1 != v:
            print("," ,end=" ")
    print()
    print("추가정보:",end="")
    count = 1
    for key , val in metadata.items():
        print("",key,"=", val,end="")
        if len(metadata) - count:
            print(",", end="")  
            count += 1
        
        
        
generate_profile("지민",26,gender="여성",*["여행","사진","독서"], job ="디자이너", country = "한국")