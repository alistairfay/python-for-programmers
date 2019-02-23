'''age=input("What is your age?: \n")
print("Your age is "+age+" years old")
'''

'''
try:
    age=int(input("enter age"))
    print("Valid age")
except Exception:
    print("You need to provide a valid number")
'''

'''
def hello():
    """ prints out helloworld to the world"""
    print("Hello World")
    print("It smells nice outside")

hello()
'''
#lettergrade

def calcthegrade(): # must define before use
    '''print the studentname and what grade they got'''
    percent=score/pointspossible*100
    print(percent)
    print(round(percent))
    if 90<=percent<=100:
        grade="A"
    elif 80<=percent<=89:
        grade="B"
    elif 70<=percent<=79:
        grade="C"
    elif 60<=percent<=69:
        grade="D"
    elif 0<=percent<=59:
        grade="F"
    else:
        grade="BORK"
    print("{} - {}".format(studentname, grade))

pointspossible=100
studentname=input("What is your name?:\n")

try:
    score=int(input("What score did you get?:\n"))
    calcthegrade()
except Exception:
    print("Please provide valid number")
