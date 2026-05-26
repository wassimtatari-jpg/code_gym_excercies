#Write a program that creates a list of tree names, 
# then uses a loop and the enumerate() function 
# to display each element of the list and its index.

tree_names=["Apple","Cherry","Lemmon"]

for index,element in enumerate(tree_names,start=1):

    print(f"Index : {index} , Element : {element}")