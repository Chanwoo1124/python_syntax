text = "apple banana orange apple kiwi apple apple"
count = 0
index = 0
location = []
word = ""
find = input("찾는 문자열을 입력하세요:")

for t in text:
    if t == " ":
        word = ""
        index += 1
    else:
        if t == " ":
            continue
        word += t
        
    if find == word:
        count += 1
        location += [index]
    
    
print(f"'{find}'은 총 {count} 등장합니다.")
print(f"위치 (인덱스): {location}")
            

