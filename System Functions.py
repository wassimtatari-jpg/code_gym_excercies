string="wassim"
number=100
number2=10.10
my_list=[10,20,30]
my_tuple=(40,50,60)
my_set={70,80,90}
my_dict={"a":100,"b":120,"c":140}
print("unique identifiers of objects :")
print(id(number))
print(id(number2))
print(id(string))
print(id(my_list))
print(id(my_tuple))
print(id(my_set))
print(id(my_dict))
print("values of hashable objects : ")
print(hash(string))
print(hash(number))
print(hash(number2))
print(hash(my_tuple))
print("list of attributes and methods of the object :")
print(dir(string))
print(dir(number))
print(dir(number2))
print(dir(my_list))
print(dir(my_dict))
print(dir(my_set))
print(dir(my_dict))