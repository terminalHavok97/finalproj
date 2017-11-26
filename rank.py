class Ranker:
    #Make the table, define the structure of a row
    #Row = id, rank, data(not sure if string or array)
    def __init__(self):
        self.table = []
        self.t_length = 0

    #Add a new sentance to the table
    def addToTable(self, data):
        l = [self.t_length, 0, data]
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
            print i[0], i[1], i[2]

        print ""
        print "===================="
        print "Total elems in table = ", self.t_length

    #Search table for data matching param data and return its id
    def getID(self, data):
        for i in self.table:
            if i[2] == data:
                return i[0]
        print "Error - Data not found"
        return -1
    #Search table for id matching param id and return its data
    def getData(self, ID):
        return self.table[ID][2]

    #Search table for id matching param id and return its rank
    def getRank(self, ID):
        return self.table[ID][1]

    #Update the ranks of ID1 and ID2 - ID1 is the victor
    #1 point for win, 0 for loss
    def updateFromComparison(self, ID1, ID2):
        k = 20

        ea1 = 1 / (1 + (10 ^ ((self.getRank(ID2) - self.getRank(ID1)) / 400)))
        ea2 = 1 / (1 + (10 ^ ((self.getRank(ID1) - self.getRank(ID2)) / 400)))

        #print "ea1 = ", ea1
        #print "ea2 = ", ea2

        rank1 = self.getRank(ID1) + (k * (1 - ea1))
        rank2 = self.getRank(ID2) + (k * (-1 - ea2))

        #print "rank1 = ", rank1
        #print "rank2 = ", rank2

        self.table[ID1][1] = rank1
        self.table[ID2][1] = rank2


    #Update rank of sentance with param id
    def __updateRank(self, ID):
        return -1
