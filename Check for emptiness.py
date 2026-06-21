def check_empety(d):
    return len(d)==0

dict1={}
dict2={"a":1}
dict3={"b":2,"c":3}
dict4={"d":4,"g":5,"n":7}
dictonaries=[dict1,dict2,dict3,dict4]

for i,d  in enumerate(dictonaries,1):
    print(f"diconarie{i} : {d} elments")
    if check_empety(d):
        print(f"the diconarie{i} is empty")
    else:
        print(f"the diconarie {i} is not empty")