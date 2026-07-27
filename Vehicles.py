class Vehicel:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicel):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model
    def drive(self):
        return f"{self.brand},{self.model} is Driving"
class Motorcycle(Vehicel):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model
    def ride(self):
        return f"{self.brand},{self.model} is Riding"

car=Car("Dacia","Jogger")
print(car.drive())

motocycle=Motorcycle("Yamaha","N88")
print(motocycle.ride())


        
