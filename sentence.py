class Sentencer:
    try:
        import random
        from textstat.textstat import textstat
    except ImportError:
        raise ImportError('<Sentencer import error>')
    global random, textstat

    #Read in word lists
    def __init__(self):
        self.nouns      = self.__readWords("assets/nouns.txt")
        self.verbs      = self.__readWords("assets/verbs.txt")
        self.adjs       = self.__readWords("assets/adjs.txt")
        self.atten      = self.__readWords("assets/fish.txt")

    #Return the result of __getSentence as an array
    def getSentenceArray(self):
        return self.__getSentence()

    #Return the result of __getSentence as a string
    def getSentenceString(self):
        array = self.__getSentence()
        string = array[0] + " " + array[1] + " " + array[2] + " " + array[3]
        return string

    #Give the user a sentance
    #Assuming SUBJECT VERB ADJ NOUN structure
    def __getSentence(self):
        while (True):
            noun1 = self.nouns[self.__randomWord(self.nouns)]
            noun2 = self.nouns[self.__randomWord(self.nouns)]
            verb = self.verbs[self.__randomWord(self.verbs)]
            adj  = self.adjs[self.__randomWord(self.adjs)]

            if (noun1 != noun2) and self.__countSyllable(verb) and self.__countSyllable(adj):
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
        return random.randrange(0, len(list), 1)

    #Count syllables in a word, return true if 1, false if else
    def __countSyllable(self, word):
        result = textstat.syllable_count(word)
        if result == 0.9:
            return True
        else:
            return False
