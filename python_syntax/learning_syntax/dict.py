bar = {"std1" : 10, "std2" : 20, "std3" : 30}

# keys = bar.keys()

# if "std1" in keys:
#     print("True")

# else:
#     print("False")

# print(bar.setdefault("std4",200))
# print(bar.setdefault("std1",100))
# print(bar)

# keys = bar.keys()
# if "std4" in keys:
#     print(bar["std4"])
  
# print(bar.get("std4")) 
# print(bar.get("std1"))
# print(bar.get("std5", False))   


# del bar["std4"]
# print(bar)
# print(bar.pop("std4", False))    
# print(bar)

# for item in bar:
#     print(item)
    
# for key,item in bar.items():
#     print(key,item)

# for key in bar.keys():
#     print(key)

# for value in bar.values():
#     print(value)
    
def prt(**kwargs):
    for key in kwargs.keys():
        print(f"key: {key}")

prt(**bar)