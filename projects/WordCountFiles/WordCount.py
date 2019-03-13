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


def process_input():
    if len(sys.argv) != 2 or len(sys.argv[1].split(".")) != 2:
        sys.exit(
            "Please call this script passing exactly 1 argument (a path to a text file e.g. myfile.txt)!!!")
    else:
        input_file = sys.argv[1]
        split = input_file.split(".")
        output_file = split[0]+"-count."+split[1]
        return [input_file, output_file]


def read_file(filename):
    inputfile = open(filename, "r")
    text = inputfile.read()
    return text


def create_word_list(text):
    wordlist = []
    for word in text.split():
        wordlist.append(word)
    return wordlist


def print_output(mywordsdict, filename):
    f = open(filename, "w+")
    f.write("There are a total of {} words\n".format(
        mywordsdict.return_total()))
    f.write("There are a {} unique words\n".format(
        mywordsdict.return_unique()))
    f.write("Here is the ordered list of words:\n")
    mywords_list_of_tuples = mywordsdict.return_sorted()
    for item in mywords_list_of_tuples:
        f.write(item[0]+" - "+str(item[1])+"\n")


def main():
    filenames = process_input()
    input_file = filenames[0]
    output_file = filenames[1]
    text = read_file(input_file)
    wordlist = create_word_list(text)
    mywordsdict = WordsDictClass.WordsDict()
    for word in wordlist:
        mywordsdict.add_word(word)
    print_output(mywordsdict, output_file)


if __name__ == "__main__":
    main()
