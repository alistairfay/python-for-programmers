class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        return 2016 - self.year
        
class Mustang(Car):
    def __init__(self, year):
        self.year = year
        self.make = "ford"
        self.model = "Mustang"

car1=Car(1991, "ford", "fiesta")
print(car1)
car2=Mustang(1991)
print(car2)
