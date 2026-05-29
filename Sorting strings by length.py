strings=[]

for _ in range(5):
    string=input("Enter a string : ")
    strings.append(string)

sorted_list=sorted(strings,key=len)

print("Sorted list :")

for string in sorted_list:
    print(string)