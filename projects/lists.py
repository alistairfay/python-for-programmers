#Lists

favgames=["mario bros 3", "earth bound", "pilot wings", "mario party", 5.8, True]

print(favgames)
print(favgames[-1])

favgames.append("zelda")
print(favgames)

favgames.insert(2, "zelda2")
print(favgames)

favgames[2] = "earth bound EDITED"
print(favgames)

del(favgames[2])
print(favgames)

favgames.remove(5.8)
favgames.remove(True)
print(favgames)

print(len(favgames))

shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]

def addtofront(my_list, my_value):
    my_list.insert(0, my_value)

addtofront(shoes, "White Vans")

print(shoes)

#Tuples - a list that can't be changed (immutable)

favgames=["mario bros 3", "earth bound", "pilot wings", "mario party"]
print(type(favgames))
print(favgames[1])
favgames.insert(1, "newgame")
print(favgames)
favgames=("mario bros 3", "earth bound", "pilot wings", "mario party")
print(type(favgames))
print(favgames[1])
#favgames.insert(1, "newgame")
print(favgames)

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    new_tuple=thetuple+(value,) # here the , makes the singleton a tuple
    print(new_tuple)
    return new_tuple

appendtotuple(shoes, "cats")

# Sets - like a list but elements must be unique,
# also there is no structured order, so no indexing

favgames=["mario bros 3", "earth bound", "pilot wings", "mario party", "mario party"]
print(favgames)

favgames=set(["mario bros 3", "earth bound", "pilot wings", "mario party", "mario party"])
print(favgames)
favgames.add("Zelda")
print(favgames)
favgames.remove("Zelda")
print(favgames)
# favgames.remove("BORK") - would break because it's not calcthegrade
favgames.discard("BORK") # - ignores if not there
