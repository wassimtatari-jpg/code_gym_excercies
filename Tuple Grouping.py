elements=tuple(input(f"Enter six elements to creat a tuple {i+1} : ") for i in range (6))

tuple_1=elements[:2]
tuple_2=elements[2:4]
tuple_3=elements[4:]

updated_tuple=tuple_1+tuple_2+tuple_3

print("Updated tuple :",updated_tuple)