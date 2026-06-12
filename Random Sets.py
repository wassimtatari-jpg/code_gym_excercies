import random

list_1=[random.randint(0,99) for _ in range(100)]

list_2=[random.randint(50,125) for _ in range(100)]

set_1=set(list_1)

set_2=set(list_2)

combein_set=set_1.union(set_2)

print(len(combein_set))