# classes and variables

class Dog:
    doginfo="Dogs are animals with 3 legs and a tail"
    #methods are just functions inside  class
    def __init__(self): # init method called every time we create an instance of a class
        print("Hey There")


dog1 = Dog()
dog1.name="Fido"
dog2 = Dog()
dog2.name="Sean"
dog3 = Dog()
dog3.hellojohn="Jane"

print(dog1.name)
print(dog2.name)
print(dog3.hellojohn)
print(dog1.doginfo)
print(dog2.doginfo)
print(dog3.doginfo)
print(Dog.doginfo) # note the class name including capital letter

Dog.doginfo="Hello"
print(dog1.doginfo)
print(dog2.doginfo)
print(dog3.doginfo)
print(Dog.doginfo) # note the class name including capital letters
