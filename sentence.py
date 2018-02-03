class Sentencer:
    try:
        import random
        from textstat.textstat import textstat
    except ImportError:
        raise ImportError('<Sentencer import error>')
    global random, textstat

    #Read in word lists
    def __init__(self):
        self.maxCycles  = 1000
        self.nouns      = self.__readWords("assets/nouns.txt")
        self.verbs      = self.__readWords("assets/verbs.txt")
        self.adjs       = self.__readWords("assets/adjs.txt")
        self.atten      = self.__readWords("assets/fish.txt")

    #Return an array of n sentances
    def getNSentences(self, n):
        array = []
        correct = False
        cycles = 0
        for i in range(0, n):
            array.append(__getSentence())

        while (correct == False):
            cycles += 1
            if (cycles >= self.maxCycles):
                raise Exception("Error - Can't generate data without duplications, consider using a bigger dataset")
            check = __findDuplicates(array, n)
            if (check.length == 0):
                correct = True
            else:
                #Remove sentances at indexs in check and replace with new sentances
                for i in check:
                    


        return array

    #Find and remove any duplicate sentances in an array of sentances
    #Returns 0 if correct, -n of duplicates otherwise
    def __findDuplicates(self, array, n):
        no = []
        for i in range(0, n):
            for j in range(0, n):
                if (i == j):
                    pass
                if (array[i] != array[j]):
                    for k in no:
                        if (i == k || j == k):
                            pass
                        else:
                            print "Duplicates detected, regenerating input"
                            no.append(i)
        return no




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
