import random

first_set={random.randint(1,20) for _ in range(10)}

second_set={random.randint(10,30) for _ in range(10)}


differce_set=first_set.difference(second_set)

symmetric=first_set.symmetric_difference(second_set)
print("first set",first_set)
print("second set",second_set)
print("the differce is",differce_set)

print("the symmetric difference",symmetric)
