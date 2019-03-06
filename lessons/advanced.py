#none

def searchstring(search):
    return None

print(searchstring(""))

def square(number):
    if type(number) == float or type(number) == int:
        return number*number
    else:
        return None

print(square(1))
print(square(1.5))
print(square("this"))

# import

import hello # we're importing a .py file from the same directory
hello.FunStuff.havefun() # we always have to reference hello.FunStuff

from hello import FunStuff # we're importing the Funstuff method from the hello file
FunStuff.havefun()

#files create read write

file=open("fun.txt", "w")
file.write("Hello my name is Al\nThis is my new file.")

# file=open("fun.txt", "w") # this will overwrite the initial file

file=open("fun.txt", "r")
print(file.read())


