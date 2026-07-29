class Animal:
    def speak(self):
        return "Rrrr!"
class Dog(Animal):
    def speak(self):
        return super().speak() + "Woof Woof"
dog=Dog()
print(dog.speak())