set_1=set(map(int,input("Enterfirst set elements sperated by space :").split()))

set_2=set(map(int,input("Enter  second set elements sperated by space : ").split()))

unite_sets=set_1|set_2

print("The unite of two sets is : ",unite_sets)

intersection=set_1.intersection(set_2)

print("the intersection between sets is ",intersection)