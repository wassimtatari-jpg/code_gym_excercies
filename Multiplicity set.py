initial_set=set()

for _ in range(5):
    numbers=input("Enter 5 numbers : ")
    numbers_set={numbers}
    initial_set.update(numbers)
print(initial_set)