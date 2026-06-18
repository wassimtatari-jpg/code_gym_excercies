fre_list=frozenset([1,2,3,4])
fre_string=frozenset("world")

print(fre_list|fre_string)
print(fre_list&fre_string)
print(fre_list-fre_string)
print(fre_list^fre_string)