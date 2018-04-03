#!/usr/bin/python
#Tom Vaughan - tv15461

class Ranker:
    try:
        import random
        import os
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError('<Ranker import error>')
    global random, os, np, plt

    #TABLE DATA
    #t[0] = ID
    #t[1] = Data (sentence)
    #t[2] = Rank
    #t[3] = Number of comparisons
    #t[4] = Interest score

    #Initialise table
    def __init__(self, percent=10):
        self.table = []
        self.t_index = 0
        self.fname = 'output/table'
        self.w_index = 0
        self.plays = 0
        self.treshhold = 0
        self.chop_size = 0
        self.percent = percent

    #Add sentence to table
    def addToTable(self, data):
        l = [self.t_index, data, 1000.0, 0, 0]
        self.table.append(l)
        self.t_index += 1
        self.threshhold = len(self.table) * self.percent
        self.chop_size = int(round(len(self.table) / self.percent))

    #Add n sentences to table
    def addAllToTable(self, array):
        for i in range(0, len(array)):
            self.addToTable(array[i])

    #Remove sentence with ID from table
    def removeFromTable(self, ID, prune=False):
        if ID > self.t_index or ID < 0:
            raise Exception("Error - ID out of bounds")
        else:
            del self.table[ID]
            self.t_index -= 1
            for i in self.table:
                if i[0] > ID:
                    i[0] -= 1
        #Don't update threshhold and chop_size if we're not pruning to maintain an
        #   adjustable max-size of the table, so it chops down easily
        if not prune:
            self.threshhold = len(self.table) * self.percent
            self.chop_size = int(round(len(self.table) / self.percent))

    #Print everything in the table
    def printAll(self):
        print "======================"
        print "ID == Data == Rank == Comparisons == Interest == Bin"
        print ""
        for i in self.table:
            print i[0], i[1], i[2], i[3], i[4]

        print ""
        print "======================"
        print "Total elems in table = ", self.t_index
        print "Total plays of elems = ", self.plays
        print "Selection threshhold = ", self.threshhold
        print "======================\n"

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

    #Get interest score from ID
    def getIntrestScore(self, ID):
        return self.table[ID][4]

    def getBin(self, ID):
        return self.table[ID][5]

    def getAllID(self):
        return False

    def getAllData(self):
        return False

    def getAllRank(self):
        rank = []
        for i in range(0, self.t_index):
            rank.append(self.table[i][2])

        return rank

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

        #Check if threshhold * 2 (or more) reached, if so, prune
        self.plays += 1
        if (self.plays > self.threshhold and self.plays % self.threshhold == 0):
            self.__prune()

    #Update n comparisons into the table where each elem is an array with two elements.
    #In 2nd array, 0th index is ID of victor, 1st index is ID of loser
    def updateNFromComparison(self, array):
        for i in array:
            self.updateFromComparison(i[0], i[1])

    #Sort the ranks in self.table into a list by rank
    #l[0] = id
    #l[1] = rank
    def __returnSortedRanks(self):
        l = []
        for i in range(0, self.t_index):
            l.append([self.table[i][0], self.table[i][2]])

        result = sorted(l, key=lambda x: x[1])
        return result

    #Updates the interest score of the table
    #Interest score calculated based off sum of neighbours plus sum of (neighbours + 1) / 2
    def __updateInterestScores(self):
        ranks = self.__returnSortedRanks()

        for i in range(0, len(ranks)):
            if (i == 0):
                self.table[i][4] = abs(ranks[i][1] - ranks[i+1][1]) * 2.0
                self.table[i][4] = abs(ranks[i][1] - ranks[i+2][1])
            elif(i == 1):
                self.table[i][4] += abs(ranks[i][1] - ranks[i+2][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i+1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-1][1])
            elif(i == (len(ranks) - 1)):
                self.table[i][4] = abs(ranks[i][1] - ranks[i-1][1]) * 2.0
                self.table[i][4] = abs(ranks[i][1] - ranks[i-2][1])
            elif(i == len(ranks) - 2):
                self.table[i][4] += abs(ranks[i][1] - ranks[i+1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-2][1])
            else:
                self.table[i][4] += abs(ranks[i][1] - ranks[i+2][1]) * 0.5
                self.table[i][4] += abs(ranks[i][1] - ranks[i+1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-2][1]) * 0.5

    #Returns two distinct random sentences
    def __find2Random(self):
        counter = 0
        l1 = self.table[random.randrange(0, len(self.table), 1)][0]
        l2 = self.table[random.randrange(0, len(self.table), 1)][0]

        while ((l1 == l2) and (counter < 1000)):
            l1 = self.table[random.randrange(0, len(self.table), 1)][0]
            l2 = self.table[random.randrange(0, len(self.table), 1)][0]
            counter += 1

        if (counter >= 1000):
            raise Exception("Error - Can't pick two random sentences from table")

        result = []
        result.append(l1)
        result.append(l2)
        return result

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

    def __returnIDFromRandomWeighting(self, r):
        total = 0
        for i in range(0, self.t_index):
            this = self.table[i][4]
            if (r >= total and r <= (total + this)):
                return self.table[i][0]
            else:
                total += this
        raise Exception("Error - Random weight couldn't be found in table")

    def __findNMostClustered(self, n):
        #1  Sum all the intrest scores
        total_sum = 0
        for i in self.table:
            total_sum += i[4]

        #2  Pick a random pair with each sentence choice weighted by the interest scores
        #3  Check that choosen pair falls within constraints of stuff already picked
        pairs = []
        for i in range(0, n):
            count = 0
            while True:
                r = random.uniform(0, total_sum)
                l1 = self.__returnIDFromRandomWeighting(r)
                r = random.uniform(0, total_sum)
                l2 = self.__returnIDFromRandomWeighting(r)

                check = True
                if (len(pairs) > 0):
                    for i in range(0, len(pairs)): #Is this pairing already in our pairs list?
                        if (((l1 == pairs[i][0]) and (l2 == pairs[i][1])) or ((l2 == pairs[i][0]) and (l1 == pairs[i][1]))):
                            check = False
                            break

                    if (l1 != l2 and check == True): #Is this pair valid?
                        break

                    if (count >= 1000):
                        raise Exception("Error - Failed to break out of while loop when finding N most interesting")
                    count += 1
                else:
                    break

            pairs.append([l1, l2])
            print ""
        return pairs

    #Find n pairs where there is a 0.5 chance of either sentence being above the 1st STDEV
    #   and the pairs are then choosen randomly from their respective partitions, while
    #   pairs aren't duplicated in the list
    def __findNRandomRanked(self, n):
        ranks = self.getAllRank()
        ranks = np.sort(ranks)
        threshhold = np.mean(ranks) + np.std(ranks)
        pairs = []
        high = []
        low = []

        def addToList(pickList1, pickList2, choosenList):
            #Choose random sentence from list1 and list2, checking it isn't already in choosenList
            count = 0
            while True:
                l1 = random.choice(pickList1)
                l2 = random.choice(pickList2)

                check = True

                if (len(choosenList) > 0):
                    '''for i in range(0, len(choosenList)):
                        if (((l1 == choosenList[i][0]) and (l2 == choosenList[i][1])) or ((l2 == choosenList[i][0]) and (l1 == choosenList[i][1]))):
                            print "Already exists"
                            print l1, l2
                            print choosenList[i][0], choosenList[i][1]
                            print ""
                            check = False
                            break'''

                    if (l1 != l2 and check == True):
                        check = False
                        break

                    if (count >= 1000):
                        raise Exception("Error - Failed to break out of while loop while finding N random ranked")
                    count += 1
                else:
                    if (l1 != l2):
                        break

            print [l1, l2]
            return [l1, l2]


        for i in range(0, self.t_index):
            if (self.table[i][2] >= threshhold):
                high.append(self.table[i][0])
            else:
                low.append(self.table[i][0])

        for i in range(0, n):
            r = random.randint(0, 3)
            if (r == 0):
                #2 lows
                print "low low"
                pairs.append(addToList(low, low, pairs))
            elif (r == 1):
                # l1 low, l2 high
                print "low high"
                pairs.append(addToList(low, high, pairs))
            elif (r == 2):
                # l1 high, l2 low
                print "high low"
                pairs.append(addToList(high, low, pairs))
            elif (r == 3):
                # 2 highs
                print "high high"
                pairs.append(addToList(high, high, pairs))
            else:
                raise Exception("Dice incorrecltly configured")

        return pairs

        '''print ranks
        print np.mean(ranks)
        print np.std(ranks)
        print "====="
        for i in ranks:
            if (i > (np.mean(ranks) + np.std(ranks))):
                print i
        plt.hist(ranks)
        plt.show()'''


    #Choose the n most interesting pairs
    def pickPairs(self, n):
        #Print out ranks
        ranks = self.__returnSortedRanks()

        pairs = []
        #If there have been at least t_index * 10 comparisons
        #   pick the two least played sentences
        if (self.plays < self.threshhold):
            print "Simple pair picking"
            for i in range(0, n):
                pairs.append(self.__find2LeastPlayed())
                self.table[pairs[i][0]][3] += 1 #Artifically boost plays
                self.table[pairs[i][1]][3] += 1

            for p in pairs: #Reset plays
                self.table[p[0]][3] -= 1
                self.table[p[1]][3] -= 1

        else: #Afterwards, pick pairs based on how many similar neighbours they have
            #self.updateInterestScores()
            #pairs = self.__findNMostClustered(n)
            print "Complex pair picking"
            pairs = self.__findNRandomRanked(n)

        return pairs

    def __prune(self):
        ranks = self.getAllRank()
        ranks = np.sort(ranks)
        stdev = np.mean(ranks) + np.std(ranks)
        lows = []

        #In all arrays here -> [id, rank]

        #0. Populate sublist of high-scoring rows
        for i in range(0, self.t_index):
            if (self.table[i][2] <= stdev):
                lows.append([i, self.table[i][2]])

        print "Begining prune"

        #1. Update interest scores
        self.__updateInterestScores()

        #2. Remove the self.chop_size most clustered rows with a bias away from
        #   above the 1st stdev (Bias is 1/2 chance to exclude > 1st stdev)

        for i in range(0, self.chop_size):
            r = random.randint(0, 1)
            if (r == 0): #Take lowest cluster score in entire table
                highest = [-1, float("-inf")]
                for j in range(0, self.t_index):
                    if (self.table[j][2] > highest[1]):
                        highest[1] = self.table[j][2]
                        highest[0] = j
                print "Removing id=" + str(highest[0]) + " rank=" + str(highest[1]) + " A"
                self.removeFromTable(highest[0], True)

            else: #Take lowest cluster score in all of table lower than 1st stdev
                highest = [-1, float("-inf")]
                for j in range(0, len(lows)):
                    if (lows[1] > highest[1]):
                        highest[1] = lows[1]
                        highest[0] = j
                print "Removing id=" + str(highest[0]) + " rank=" + str(highest[1]) + " L"
                self.removeFromTable(highest[0], True)


    #Returns a list containing the highest rank in the table and the lowest
    def __getHighestAndLowestRank(self):
        result = [float("-inf"), float("inf")]
        for i in self.table:
            if (i[2] > result[0]):
                result[0] = i[2]
            if (i[2] < result[1]):
                result[1] = i[2]
        return result

    #Break up distribtion of ranks into evenly sized bins, then put each rank in a bin
    def __createBins(self):
        return False

    def __findNMost(self, n):
        return False

    def exportAsGraph(self):
        ranks = []
        for i in range(0, self.t_index):
            ranks.append(float(self.table[i][2]))

        result = sorted(ranks)

        for i in result:
            print i

        if (result[0] > result[10]):
            print "WRONG"

        #plt.plot(result, 'ro')
        plt.hist(result, 'auto')
        plt.show()

    #Load a table that was previously saved into our current one
    def importTable(self, path):
        s = []
        count = -1
        #f = open(path, 'r')

        with open(path, 'rb') as f:
            for line in f:
                l = line.strip()
                if (l == ""):
                    print "BLANK"
                else:
                    print l
                    if (count == -1):
                        self.percent = int(l)
                    elif (count == 0 or count == 3):
                        s.append(int(l))
                    elif (count == 2 or count == 4):
                        s.append(float(l))
                    elif (count == 1):
                        s.append(str(l))

                    if (count == 4):
                        count = 0
                        self.table.append(s)
                        self.t_index += 1
                        s = []
                    else:
                        count += 1
            print "EOF\n"
            self.threshhold = self.percent * len(self.table)
            self.chop_size = int(round(len(self.table) / self.percent))

            for i in self.table:
                self.plays += i[3]

            if (self.plays > self.threshhold and self.plays % self.threshhold == 0):
                self.__prune()

            f.close()

    #Export a copy of the table after dividing data into seperate bins for analysis
    def exportData(self):
        f = open((str(self.fname) + str(self.w_index) + ".txt"), 'w')
        self.w_index += 1
        f.write(str(self.percent) + "\n")
        for i in range(0, len(self.table)):
            for j in range(0, 5):
                if (j == 1):
                    for k in range(0, 4):
                        f.write(str(self.table[i][j][k] + ' '))
                    f.write('\n')
                else:
                    f.write(str(self.table[i][j]) + '\n')
            f.write('\n')
        f.close()
