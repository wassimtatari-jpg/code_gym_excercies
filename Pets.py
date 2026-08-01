class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass
def check(obj):
    return isinstance(obj,Animal)

dog=Dog()
cat=Cat()
not_animal="NOt animal"

print(check(dog))
print(check(cat))
print(check(not_animal))