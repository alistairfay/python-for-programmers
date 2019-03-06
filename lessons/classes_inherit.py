# classes and variables
class Car:
    def __init__(self, year, make, model):
        self.year=year
        self.make=make
        self.model=model

    def age(self):
        return 2016-self.year
        
class Mustang(Car):
    def __init__(self, year, make, model):
        self.year=year
        self.make="Ford"
        self.model="Mustang"

class Dog:
    #methods are just functions inside  class
    def __init__(self, name, age, furcolor): # init method called every time we create an instance of a class
        self.name=name
        self.age=age
        self.furcolor=furcolor

    def barkhello(): # class method as doesn't reference self
        print("Hello World")

    def barkgoodbye(self): # instance method as references self
        print("goodbye world")

class Bulldog(Dog): # here we're defining a subclass of the Dog class where we inherit all the properties/methods but can add some more
    "hello"

    def growl(self):
        print("grrrr")

dog1 = Dog("fido", 8, "brown")
print(dog1.age)
# dog1.barkhello() # this fails as it's a class method and we're calling as an instance method
Dog.barkhello() # this works because it's a class method and we're calling as a class method
# Dog.barkgoodbye() # this fails as it's an instance method and we're calling as a class method
dog1.barkgoodbye() # this works as it's an instance method and we're calling as an instance method
dog2=Bulldog("Mike", 22, "white")

print(dog2)
print(dog2.name)
dog2.barkgoodbye()
dog2.growl()
# dog1.growl() this will fail as the dog object has no growl method (only the subclass Bulldog)

