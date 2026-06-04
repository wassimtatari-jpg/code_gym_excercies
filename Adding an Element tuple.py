elements=tuple(input(f"Enter five elments {i+1} : ") for i in range (5))

new_element=input("Enter new element to add to the end of  your tuple : ")

updated_tuple=elements+(new_element,)

print("Updated tuple : ", updated_tuple)