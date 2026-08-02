def subclass(class1,class2):
    return issubclass(class1,class2)
class Vecihle:
    pass
class Car(Vecihle):
    pass
class Byicecle(Vecihle):
    pass

print(subclass(Car,Vecihle))
print(subclass(Byicecle,Vecihle))