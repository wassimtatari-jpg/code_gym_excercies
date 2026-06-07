my_tuple=((1,2,3),(4,5,6),(7,8,9))

total=0

for inside_tuple in my_tuple:
    for num in inside_tuple:
        total+=num

print("the sum of elment is ",total)
