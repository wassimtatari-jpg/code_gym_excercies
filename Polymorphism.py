class Shape:
    def perimetre(self):
        raise NotImplementedError("subclasses shoud implement this method!!!")
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimetre(self):
        return self.a+self.b+self.c
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def perimetre(self):
        return 2*(self.a+self.b)
shapes=[Triangle(5,7,8),Rectangle(5,6),Triangle(10,20,35),Rectangle(8,9)]
perimeters=[shape.perimetre()for shape in shapes]

for perimetre in perimeters:
    print(perimetre)
        
        
   