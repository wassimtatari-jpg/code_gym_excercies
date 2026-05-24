my_list=[50,60,70,80,90]

index_element_remove=int(input("Enter the index of element that you want remove : "))

if 0<=index_element_remove<len(my_list):
    removed_element=my_list.pop(index_element_remove)
    print("Removed element : ",removed_element)
    print("Updated list : ",my_list)
else:
    print("The index does not exist")