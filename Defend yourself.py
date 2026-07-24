class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self._model=model
    def get_model(self):
        return self._model
    def set_model(self,model):
        self._model=model
car=Car("Toyota","Yariss")

car.brand="dacia"

car.set_model("jogger")

print(f"Brand {car.brand} model {car.get_model()}")
