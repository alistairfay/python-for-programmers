# parameters

def addtwo(num1, num2):
    print(num1+num2)

addtwo(4,6)

def firstletter(inputstring):
    print(inputstring[:1])

firstletter("test")

def madlib(name, verb, noun):
    print(name + " was " + verb + " with " + noun + "!")

madlib("aldo", "running", "cheese")
madlib("cheese", "aldo", "running")
madlib(name="aldo", verb="running", noun="cheese")
madlib(verb="running", name="aldo", noun="cheese")
#madlib() - borks because no parameters

def madlib(name="aldo", verb="eating", noun="cheese"):
    print(name + " was " + verb + " with " + noun + "!")

madlib()
madlib(verb="running")

def madlib(name, verb, noun, *thelastones):
    print(name + " was " + verb + " with " + noun + "!")
    print(thelastones)

madlib("aldo", "running", "cheese", 1, 2, 3, 4, "five")

def add2(num1, num2):
    total=num1+num2
    return total
    print("never shows due to return")

thenum=add2(3,6)

def printtype(input_param):
    if(isinstance(input_param, str)):
        return "String"
    elif(isinstance(input_param, int)):
        return "Int"
    elif(isinstance(input_param, float)):
        return "Float"
    else:
        return "BORK"


print(printtype("string"))
print(printtype(1))
print(printtype(1.5))
