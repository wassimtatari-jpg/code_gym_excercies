string=input("enter your string : ")
length=len(string)
print(f"the length is : {length}")

user_index=int(input("Enter your index : "))

if user_index<0 or user_index>=len(string):
    print("The index is outpunds ")
else:
    print(f"your index {user_index} present the charcter {string[user_index]}")