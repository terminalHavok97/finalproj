#!/usr/bin/python
#Tom Vaughan - tv15461

class Ranker:
    try:
        import random
        import os
    except ImportError:
        raise ImportError('<Ranker import error>')
    global random, os

    #TABLE DATA
    #t[0] = ID
    #t[1] = Data (sentence)
    #t[2] = Rank
    #t[3] = Number of comparisons

    #Initialise table
    def __init__(self):
        self.table = []
        self.t_index = 0

    #Add sentence to table
    def addToTable(self, data):
        l = [self.t_index, data, 1000.0, 0]
        self.table.append(l)
        self.t_index += 1

    #Add n sentences to table
    def addAllToTable(self, array):
        for i in range(0, len(array)):
            self.addToTable(array[i])

    #Remove sentence with ID from table
    def removeFromTable(self, ID):
        if ID > self.t_index or ID < 0:
            raise Exception("Error - ID out of bounds")
        else:
            del self.table[ID]
            self.t_index -= 1
            for i in self.table:
                if i[0] > ID:
                    i[0] -= 1

    #Print everything in the table
    def printAll(self):
        print "==================="
        print "ID == Data == Rank == Comparisons"
        print ""
        for i in self.table:
            print i[0], i[1], i[2], i[3]

        print ""
        print "==================="
        print "Total elems in table = ", self.t_index
        print ""

    #Search table for data matching param data and return its id
    #-1 indicates not found, error thrown if multiple entries
    def getID(self, data):
        found = -1
        for i in self.table:
            if i[1] == data:
                if found == -1:
                    found = i[0]
                else:
                    raise Exception("Error - Concurrent elems in table")
        return found

    #Get data from ID
    def getData(self, ID):
        return self.table[ID][1]

    #Get rank from ID
    def getRank(self, ID):
        return self.table[ID][2]

    #Get comparions from ID
    def getComp(self, ID):
        return self.table[ID][3]

    #Get K value (can be changed later)
    def __getKValue(self, ID):
        return 32

    #Update the table with the results of the comparison of two IDS. ID1 was the victor
    def updateFromComparison(self, ID1, ID2, draw=False):
        self.table[ID1][3] += 1
        self.table[ID2][3] += 1

        qa = pow(10, self.getRank(ID1) / float(400))
        qb = pow(10, self.getRank(ID2) / float(400))

        ea1 = qa / (qa + qb)
        ea2 = qb / (qa + qb)

        if draw == False:
            rank1 = self.getRank(ID1) + (self.__getKValue(ID1) * (1 - ea1))
            rank2 = self.getRank(ID2) + (self.__getKValue(ID2) * (0 - ea2))
        else:
            rank1 = self.getRank(ID1) + (self.__getKValue(ID1) * (0.5 - ea1))
            rank2 = self.getRank(ID2) + (self.__getKValue(ID2) * (0.5 - ea2))

        self.table[ID1][2] = rank1
        self.table[ID2][2] = rank2

    #Update n comparisons into the table where each elem is an array with two elements.
    #In 2nd array, 0th index is ID of victor, 1st index is ID of loser
    def updateNFromComparison(self, array):
        for i in array:
            print i[0], i[1]
            self.updateFromComparison(i[0], i[1])

    #Returns the 2 least played sentences
    def __find2LeastPlayed(self):
        low_bound = float("inf")
        lows = []
        l1 = None
        l2 = None
        #Find list of joint-lowest comparisons
        for i in self.table:
            if i[3] < low_bound:
                low_bound = i[3]
                del lows[:]
                lows.append(i)
            elif i[3] == low_bound:
                lows.append(i)

        if len(lows) > 1:
            j = random.randrange(0, len(lows), 1)
            l1 = lows[j]
            del lows[j]
            k = random.randrange(0, len(lows), 1)
            l2 = lows[k]
        elif len(lows) == 1:
            l1 = lows[0]
            del lows[:]
            low_bound = float("inf")
            for i in self.table:
                if i[3] != l1[3] and i[3] < low_bound:
                    low_bound = i[3]
                    del lows[:]
                    lows.append(i)
                elif i[3] != l1[3] and i[3] == low_bound:
                    lows.append(i)
            if len(lows) > 1:
                i = random.randrange(0, len(lows), 1)
                l2 = lows[i]
            elif len == 1:
                l2 = lows[0]
            else:
                raise Exception("Error - Non 2nd least played row")
        else:
            raise Exception("Error - No least played rows")

        result = []
        result.append(l1[0])
        result.append(l2[0])
        return result

    #A naive implementation for pair picking relying only on __find2LeastPlayed
    def pickPairsNaive(self, n):
        pairs = []

        for i in range(0, n):
            pairs.append(self.__find2LeastPlayed())
            self.table[pairs[i][0]][3] += 1
            self.table[pairs[i][1]][3] += 1

        for p in pairs:
            self.table[p[0]][3] -= 1
            self.table[p[1]][3] -= 1

        return pairs

    #Choose the n most interesting pairs
    def pickPairs(self, n):
        #Assign an interestingness score to each sentence
        #Will then pick pairs which are (mostly) close to each other in this score
        result = []
        l1 = None
        l2 = None
        score = []

        for i in self.table:
            #TODO See just how good this metric is?
            score.append((i[2] / 100.0) - (10.0 / i[3]))

        #Pick top-ranked sentence
        l1 = float("-inf")


        #Pick sentence with




    def prune(self):
        #After n plays, each sentence will be able to be pruned if in the
        # bottom n % of the table -- That'll probs be 2nd STDEV
        print "PRUNE"

    #Save a copy of table in the logs dir
    def saveTable(self):
        return True

    #Export a copy of the table after dividing data into seperate bins for analysis
    def exportData(self):
        return True
