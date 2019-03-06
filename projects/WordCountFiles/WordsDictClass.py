class WordsDict(dict):

    '''
    subclass of dict expected to hold a list of words as keys and a count of their occurence asa values
    '''

    def add_word(self, word):
        '''
        adds new words to the dict with a count of 1
        increments the count of existing words by 1
        '''
        if word in self.keys():
            self[word]=self[word]+1
        else:
            self[word]=1
    
    def return_total(self):
        return sum(list(self.values()))

    def return_unique(self):
        return len(self)

    def return_sorted(self):
        import operator
        return sorted(self.items(), key=operator.itemgetter(1), reverse=True)
    