import math

class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self,redius):
        self.redius=redius
    def area(self):
        return math.pi*(self.redius**2)

rect=Rectangle(3,6)
print(f"Area of racangle is {rect.area()}")

cir=Circle(5)
print(f"Area of circle is {cir.area()}")
        
       