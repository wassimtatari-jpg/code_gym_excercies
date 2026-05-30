import random

random_list=[random.randint(1,100) for _ in range (10)]

copy=list(random_list)

copy.sort()

print("Orgianl list : ",random_list)

print("sorted list : ",copy)