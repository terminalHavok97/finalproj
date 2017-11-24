class Sentencer:
    import random

    def __init__(self):
        #Read in word lists
        self.nouns      = readWords("assets/nouns.txt")
        self.verbs      = readWords("assets/verbs.txt")
        self.adj        = readWords("assets/adjectives.txt")

    def giveSentence(self):
        #Give the user a sentance
        #Assuming SUBJECT VERB ADJ NOUN structure
        verb = self.verbs[random.choice(self.verbs)]
        adj  = self.adj[random.choice(self.adj)]
        while (noun1 != noun2):
            noun1 = self.nouns[random.choice(self.nouns)]
            noun2 = self.nouns[random.choice(self.nouns)]
        result = noun1 + " " + verb + " " + adj + " " + noun2
        return result


    def readWords(fname):
        with open(fname) as f:
            words = f.readlines()
        words = [x.strip() for x in words]
        return words
