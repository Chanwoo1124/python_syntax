l = list(input().split())

st = ""

for l_v in l:
    st += l_v
   

if st == "12345678":
        print("ascending")
        
elif st == "87654321":
        print("descending")
        
else:
        print("mixed")