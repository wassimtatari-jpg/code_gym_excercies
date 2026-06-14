import random

random_set={random.randint(1,50) for _ in range(10)}

for index,element in enumerate(random_set):
    print(f"Index : {index} , Element {element}")