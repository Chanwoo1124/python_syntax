import random
count = [0,0,0,0,0,0]
max_nam = 0

while True:
    n = int(input("Enter the number of dice rolls (betwwn 100 and 1,000,000):"))
    if not 100 <= n <=1000000:
        print("Please enter a number wiuthin the spectified range.")
    
    else:
        for _ in range(n):
            num = random.randint(1,6)
            count[num-1] += 1
    break
    # 상대적인 비율을 시각화 해야함
    

max_count = count[0]

for co in count:
    if co > max_count:
        max_count = co
print()
print("Dice Roll Frequency Histogram:")
for i_c in range(len(count)):
    star = count[i_c] * 10 // max_count
    percent = count[i_c] *100 // n
    print(f"{i_c +1}: {"*"*star} ({count[i_c]} times, {percent}%)")
            
         

        