# Hangman
# list() to get a list of characters
# .lower() to make it easier
# use functions
# global varname makes a var in a function ref the external definition

## TODO:
# far too much use of global variables
# no input validation

import time

incorrectletters=[]
word=""
chars=[]
solution=[]

def getinputs():
    global lives
    global word
    global chars
    global solution
    lives=int(input("How many lives shall we have?\n"))
    word=input("What is the word we have to guess?\n")
    #debug
    print("playing with '{}'' lives to guess the word '{}'!".format(lives, word))
    chars=list(word.lower())
    solution=["_"] * len(chars)
    print("*****************************")

def printstatus():
    print("\nYou have "+ str(lives) +" lives remaining")
    if len(incorrectletters)>0:
        print("You've already guessed these incorrect letters:")
        for index, letter in enumerate(incorrectletters):
            if index == (len(incorrectletters)-1):
                print(letter)
            else:
                print(letter, end=", ")
    print("The current solution is: ")
    for letter in solution:
        print(letter, end=" ")

def promptguess():
    global guess
    guess=input("\nGuess a character: ").lower()

def checkguess():
    global solution
    global guess
    global lives
    global won
    global incorrectletters
    hit=False
    for index, char in enumerate(chars):
        if guess == char:
            solution[index]=guess
            hit=True
            print("Well done you got one!")
            if solution == chars:
                won=True
                break
    else:
        if not hit:
            print("Sorry that wasn't one!")
            lives-=1
            incorrectletters.append(guess)
    time.sleep(2)

def showresult():
    if won:
       print("You correctly guessed " + word + " with " + str(lives) + " lives remaining") 
    else:
        print("You ran out of lives before you could guess the word " + word)

getinputs()
won=False
while not won and lives>0:
    #print status
    printstatus()
    #ask for letter
    promptguess()
    #check and see if they won
    checkguess()

showresult()
