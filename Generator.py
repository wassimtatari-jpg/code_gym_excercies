def make_counter():
    count=0
    def funcation_counter():
        nonlocal count
        count+=1
        return count
    return funcation_counter
counter_1=make_counter()
counter_2=make_counter()

print(counter_1())
print(counter_2())
print(counter_1())
print(counter_2())