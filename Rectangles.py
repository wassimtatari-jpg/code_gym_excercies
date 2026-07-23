class Rectangle:
    def __init__(self,width,heighth):
        self.width=width
        self.heighth=heighth
    def area(self):
        return self.width*self.heighth
calculat=Rectangle(5,7)

print(calculat.area())
        