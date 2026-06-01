#creat a tuple of 5 elemnts by user

elements=tuple(input(f"Enter your elements {i+1} : " ) for i in range (5))

#ask user for index

index=int(input("Enter the element index : "))

#checking operation

if 0<=index<len(elements):
    print(f"Index entered is : {index} of element {elements[index]}")
else:
    print("Index outbounds")