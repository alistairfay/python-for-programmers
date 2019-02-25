dogs={"fido":5, "rex":7, "fluffy":6}

#print whole dict
print(dogs)

#print value for given key
print(dogs["fido"])

# we can have duplicate values but not duplicate keys
# if we try to add a duplicate key the last will overwrite the first
dogs={"fido":5, "rex":7, "fluffy":7, "fido":500}
print(dogs)

#the keys need to b immutable (e.g. strings, ints, floats, tuples but not lists)

#can use different types for the keys and values
dogs={"fido":5, "rex":7, "fluffy":7, 21:"ben"}
print(dogs)
print(dogs[21])

#create a dict from two lists
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"] 
cooldictionary={}
print(cooldictionary)
for i in range(len(words)):
    cooldictionary[words[i]]=definitions[i]
print(cooldictionary)

# add update delete and loop

#add
# dogs={"fido":5, "rex":7, "fluffy":7}
dogs["hayley"]=21
print(dogs)

#update
dogs={"fido":5, "rex":7, "fluffy":7}
dogs["fido"]=21
print(dogs)

#delete
dogs={"fido":5, "rex":7, "fluffy":7}
del(dogs["fido"])
print(dogs)



#loop
print(dogs.keys())
for name in dogs.keys():
    print(name + " is " + str(dogs[name]) + " years old")

