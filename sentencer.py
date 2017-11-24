class Sentencer:
    try:
        import random
    except ImportError:
        raise ImportError('<Sentencer import error>')
    global random

    #Read in word lists
    def __init__(self):
        self.nouns      = self.readWords("assets/nouns.txt")
        self.verbs      = self.readWords("assets/verbs.txt")
        self.adjs       = self.readWords("assets/adjectives.txt")

    #Give the user a sentance
    #Assuming SUBJECT VERB ADJ NOUN structure
    def giveSentence(self):
        verb = self.verbs[self.randomWord(self.verbs)]
        adj  = self.adjs[self.randomWord(self.adjs)]
        while (True):
            noun1 = self.nouns[self.randomWord(self.nouns)]
            noun2 = self.nouns[self.randomWord(self.nouns)]
            if noun1 != noun2:
                break
        result = noun1 + " " + verb + " " + adj + " " + noun2
        return result

    #Read in a specific word list
    def readWords(self, fname):
        with open(fname) as f:
            words = f.readlines()
        words = [x.strip() for x in words]
        return words

    #Get random index in a list
    def randomWord(self, list):
        return random.randrange(0, (len(list) - 1), 1)
