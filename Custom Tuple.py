elements=[]

print("Enter your elements(Press eneter to finish) : ")

while True:
    element=input()
    if element=="":
        break
    elements.append(element)

tuple_element=tuple(elements)
if tuple_element:
    print(f"The last element in your tuple is {tuple_element[-1]}")
else:
    print("Your tuple is empety")