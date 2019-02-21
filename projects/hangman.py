# Hangman
# list() to get a list of characters
# .lower() to make it easier
# use functions
# global varname makes a var in a function ref the external definition

lives=int(input("How many lives shall we have?\n"))
word=input("What is the word we have to guess?\n")

#debug
print("playing with '{}'' lives to guess the word '{}'!".format(lives, word) )

chars=list(word.lower())
#debug
print(chars)

won=False
while not won and lives>0:
    guess=input("Guess a character?\n")
    if guess in chars:
        print("You got one")
        chars.remove(guess)
    else:
        print("nope")
        lives-=1
    if len(chars) == 0:
        won=True

if won:
    print("You correctly guessed '{}' with '{}' lives remaining".format(word, lives))
else:
    print("You ran out of lives before you could guess the word '{}'".format(word))
