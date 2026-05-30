import random

random_list=[random.randint(1,20) for _ in range(10)]

print("Orgianl list : ",random_list)

new_list=[]

for x in random_list:
    if x%2!=0:
        new_list.append(x)
print("Updated list : ",new_list)