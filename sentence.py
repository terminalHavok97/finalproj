class Sentencer:
    try:
        import random
        from textstat.textstat import textstat
    except ImportError:
        raise ImportError('<Sentencer import error>')
    global random, textstat

    #Read in word lists
    def __init__(self):
        self.maxCycles  = 10
        self.nouns      = self.__readWords("assets/nouns.txt")
        self.verbs      = self.__readWords("assets/verbs.txt")
        self.adjs       = self.__readWords("assets/adjs.txt")

    #Return an array of n sentences
    def getNSentences(self, n):
        array = []
        correct = False
        cycles = 0
        for i in range(0, n):
            array.append(self.__getSentence())

        while (correct == False):
            cycles += 1
            if (cycles >= self.maxCycles):
                raise Exception("Error - Can't generate data without duplications, consider using a bigger dataset")
            check = self.__findDuplicates(array)
            if (len(check) == 0):
                correct = True
            else:
                print "Duplicates detected - Removing and regenerating"
                #Remove sentences at indexs in check and replace with new sentences
                for i in check:
                    array[i] = self.__getSentence()

        return array

    #Returns a random sentence with one of the words as "fish"
    def __makeFishSentence(self):
        s = self.__getSentence()
        r = random.randint(0,3)
        s[r] = "fish"
        return s

    #TODO UPDATE: Takes an array of sentence pairs, and a length of array, and adds ~10% fish-containing pairs
    def fishify(self, n):
        result = []
        for i in range(0, n):
            r = random.randint(0,1)
            if (r == 0):
                result.append([-1, self.__makeFishSentence(), -1, self.__getSentence()])
            else:
                result.append([-1, self.__getSentence(), -1, self.__makeFishSentence()])
        return result

    #Find and remove any duplicate sentences in an array of sentences
    #Returns 0 if correct, -n of duplicates otherwise
    def __findDuplicates(self, array):
        n = len(array)
        no = []
        for i in range(0, n):
            for j in range(0, n):
                if (i == j):
                    continue
                if (array[i] == array[j]):
                    print "Duplicates detected " + str(i) + " " + str(j)
                    if (len(no) == 0):
                        no.append(i)
                    else:
                        for k in no:
                            if (i == k or j == k):
                                pass
                            else:
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

    #Give the user a sentence
    #Assuming SUBJECT VERB ADJ NOUN structure
    def __getSentence(self):
        while (True):
            noun1 = self.nouns[self.__randomWord(self.nouns)]
            noun2 = self.nouns[self.__randomWord(self.nouns)]
            verb = self.verbs[self.__randomWord(self.verbs)]
            adj  = self.adjs[self.__randomWord(self.adjs)]

            if (noun1 != noun2):
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
            print "Word rejected - " + str(word)
            return False
