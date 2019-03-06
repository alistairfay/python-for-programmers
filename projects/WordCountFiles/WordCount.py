'''
input - a path to a file
output - an output file which is named after the intput file with -count.txt

output file should contain 
total words
total unique words
sorted list of words with word count
hints - when counting words dictionaries are your friend
'''
import sys
import WordsDictClass

def get_input():
    if len(sys.argv) != 2:
        sys.exit("Please call this script passing exactly 1 argument (a path to a text file)!!!")

def read_file(filename):
    inputfile=open(sys.argv[1],"r")
    text=inputfile.read()
    return text

def create_word_list(text):
    wordlist=[]
    for word in text.split():
        wordlist.append(word)
    return wordlist

get_input()
text=read_file(sys.argv[1])
wordlist=create_word_list(text)
mywordsdict=WordsDictClass.WordsDict()
for word in wordlist:
        mywordsdict.add_word(word)

print("There are a total of {} words".format(mywordsdict.return_total()))
print("There are a {} unique words".format(mywordsdict.return_unique()))
print("The words appear this number of times:")
mywords_list_of_tuples=mywordsdict.return_sorted()
for item in mywords_list_of_tuples:
        print(item[0]+" - "+str(item[1]))
