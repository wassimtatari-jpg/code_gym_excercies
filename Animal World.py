class Animal:
    def make_sound(self):
        return"Uuuuuuu!"
class Dog(Animal):
    def make_sound(self):
        return super().make_sound()+"Woof Woof !!"
class Cat(Animal):
    def make_sound(self):
        return super().make_sound()+"Maou MAou !!"
dog=Dog()
cat=Cat()

print(cat.make_sound())
print(dog.make_sound())