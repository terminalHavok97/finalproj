class Ranker:
    #Make the table, define the structure of a row
    #Row = id, rank, data(not sure if string or array)
    def __init__(self):

    #Add a new sentance to the table
    def addToTable(self, data):
        return -1

    #Remove the sentence indexed id from the table
    def removeFromTable(self, id):
        return -1

    #Search table for data matching param data and return its id
    def getID(self, data):
        return -1

    #Search table for id matching param id and return its data
    def getData(self, id):
        return -1

    #Search table for id matching param id and return its rank
    def getRank(self, id):
        return -1

    #Update the ranks of
    def updateFromComparison(self, id1, id2):
        return -1

    #Update rank of sentance with param id
    def __updateRank(self, id):
        return -1
