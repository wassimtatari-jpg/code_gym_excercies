class Car:
    def __init__(self,make,made,year):
        self.make=make
        self.made=made
        self.year=year
    def display_info(self):
        print(f"car information : Make: {self.make} Made: {self.made} Year: {self.year}")

my_car=Car("dacia","jogger",2025)    
my_car.display_info()    
        