class Sentencer:
    try:
        import random
    except ImportError:
        raise ImportError('<Sentencer import error>')
    global random

    #Read in word lists
    def __init__(self):
        self.nouns      = self.__readWords("assets/nouns.txt")
        self.verbs      = self.__readWords("assets/verbs.txt")
        self.adjs       = self.__readWords("assets/adjectives.txt")

    #Give the user a sentance
    #Assuming SUBJECT VERB ADJ NOUN structure
    def getSentence(self):
        verb = self.verbs[self.__randomWord(self.verbs)]
        adj  = self.adjs[self.__randomWord(self.adjs)]
        while (True):
            noun1 = self.nouns[self.__randomWord(self.nouns)]
            noun2 = self.nouns[self.__randomWord(self.nouns)]
            if noun1 != noun2:
                break
        result = [noun1, verb, adj, noun2]
        return result

    #Read in a specific word list
    def __readWords(self, fname):
        with open(fname) as f:
            words = f.readlines()
        words = [x.strip() for x in words]
        f.close()
        return words

    #Get random index in a list
    def __randomWord(self, list):
        return random.randrange(0, (len(list) - 1), 1)
