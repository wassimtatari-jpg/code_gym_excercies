my_list=[10,20,50,30,100,40,70,80]

for i in range(1,len(my_list)):
    if my_list[i]>my_list[i-1]:
        print(f'{my_list[i]} is Gretter than {my_list[i-1]}')
    else:
        print(f'{my_list[i]} is Smaller than {my_list[i-1]}')