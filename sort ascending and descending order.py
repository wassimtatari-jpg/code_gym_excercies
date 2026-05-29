import random

random_list=[random.randint(1,100) for _ in range(10)]

ascending_list=sorted(random_list)

descending_list=sorted(random_list,reverse=True)

print("Orginal list : " ,random_list)

print("Ascending list : ",ascending_list)

print("Descending list : ", descending_list)