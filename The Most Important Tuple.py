nasted_tuple=((55,99,150),(1,4,5),(88,99,110))

max_value=float('-inf')

for iterate_tuple in nasted_tuple:
    if max(iterate_tuple)>max_value:
        max_value=max(iterate_tuple)
print("The max value in the nasted tuple is ",max_value)

