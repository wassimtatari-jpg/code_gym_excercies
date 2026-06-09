from enum import unique


elements=[]

for _ in range (10):
    element=input("Enter 10 elements : ")
    elements.append(element)

unique_elements=set(elements)

print(unique_elements)