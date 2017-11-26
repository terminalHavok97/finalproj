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
        return -1

    #Update the ranks of
    def updateFromComparison(self, id1, id2):
        return -1

    #Update rank of sentance with param id
    def __updateRank(self, ID):
        return -1
