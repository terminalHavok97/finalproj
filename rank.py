class Ranker:
    try:
        import random
    except ImportError:
        raise ImportError('<Ranker import error>')
    global random
    #Make the table, define the structure of a row
    #Row = id, rank, comparisons, data(not sure if string or array)
    def __init__(self):
        self.table = []
        self.t_length = 0

    #Add a new sentance to the table
    def addToTable(self, data):
        l = [self.t_length, 1000.0, 0, data]
        self.table.append(l)
        self.t_length += 1

    #Remove the sentence indexed id from the table
    def removeFromTable(self, ID):
        if ID > self.t_length or ID < 0:
            print "Error - ID out of bounds of table"
            return -1
        del self.table[ID]
        self.t_length -= 1
        for i in self.table:
            if i[0] > ID:
                i[0] -= 1


    #Print everything in the table
    def printAll(self):
        for i in self.table:
            print i[0], i[1], i[2], i[3]

        print ""
        print "===================="
        print "Total elems in table = ", self.t_length
        print ""

    #Search table for data matching param data and return its id
    def getID(self, data):
        for i in self.table:
            if i[3] == data:
                return i[0]
        print "Error - Data not found"
        return -1
    #Search table for id matching param id and return its data
    def getData(self, ID):
        return self.table[ID][3]

    #Search table for id matching param id and return its comparions
    def getComp(self, ID):
        return self.table[ID][2]

    #Search table for id matching param id and return its rank
    def getRank(self, ID):
        return self.table[ID][1]

    #Update the ranks of ID1 and ID2 - ID1 is the victor
    #1 point for win, 0 for loss, 0.5 for draw(on timeout)
    def updateFromComparison(self, ID1, ID2, draw=False):
        self.table[ID1][2] += 1
        self.table[ID2][2] += 1

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

        self.table[ID1][1] = rank1
        self.table[ID2][1] = rank2


    #Return a k-value appropriate for the rank of the sentance
    #Using the FIDE ranges (world chess federation)
    def __getKValue(self, ID):
        if (self.table[ID][2] < 30 and self.table[ID] < 2300):
            return 40
        elif(self.table[ID][1] < 2400):
            return 20
        else:
            return 10

    #Returns the 2 least played sentances
    def find2LeastPlayed(self):
        low_bound = float("inf")
        lows = []
        l1 = None
        l2 = None
        #Find list of joint-lowest comparisons
        for i in self.table:
            if i[2] < low_bound:
                low_bound = i[2]
                del lows[:]
                lows.append(i)
            elif i[2] == low_bound:
                lows.append(i)

        if len(lows) > 1:
            print "DEBUG: ", lows
            j = random.randrange(0, len(lows), 1)
            l1 = lows[j]
            del lows[j]
            k = random.randrange(0, len(lows), 1)
            l2 = lows[k]
        elif len == 1:
            l1 = lows[0]
            del lows[:]
            low_bound = float("inf")
            for i in self.table:
                if i[2] != l1[2] and i[2] < low_bound:
                    low_bound = i[2]
                    del lows[:]
                    lows.append(i)
                elif i[2] != li[2] and i[2] == low_bound:
                    lows.append(i)
            if len(lows) > 1:
                i = random.randrange(0, len(lows), 1)
                l2 = lows[i]
            elif len == 1:
                l2 = lows[0]
            else:
                print "Error - Non 2nd least played row"
                return -1
        else:
            print "Error - No least played rows"
            return -1

        result = []
        result.append(l1[0])
        result.append(l2[0])
        return result
