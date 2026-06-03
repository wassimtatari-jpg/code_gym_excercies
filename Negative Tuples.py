elements=[]

for i in range (7):
    element=input(f"Enter your element {i+1} : ")
    elements.append(element)

tuple_elements=tuple(elements)

print(f"The third element from the end is {tuple_elements[-3]}")

print(f"The penultimate element is {tuple_elements[-2]}")