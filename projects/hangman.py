# Hangman
# list() to get a list of characters
# .lower() to make it easier
# use functions
# global varname makes a var in a function ref the external definition

## TODO:
# create a list of blanks and print it each time
# each time they get a letter update the list of blanks to sub in the letter

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

def promptguess():
    global solution
    global guess
    print(solution)
    guess=input("Guess a character\n")

def checkguess():
    global chars
    global solution
    global guess
    global lives
    global won
    hit=False
    for index, char in enumerate(chars):
        if guess == char:
            solution[index]=guess
            hit=True
            if solution == chars:
                won=True
                break
    else:
        if not hit:
            lives-=1

def showresult():
    global won
    global word
    global lives
    if won:
        print("You correctly guessed '{}' with '{}' lives remaining".format(word, lives))
    else:
        print("You ran out of lives before you could guess the word '{}'".format(word))

getinputs()
won=False
while not won and lives>0:
    promptguess()
    checkguess()
else:
    showresult()
