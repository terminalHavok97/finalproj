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
    #t[4] = Interest score

    #Initialise table
    def __init__(self):
        self.table = []
        self.t_index = 0
        self.fname = 'output/table'
        self.w_index = 0
        self.plays = 0

    #Add sentence to table
    def addToTable(self, data):
        l = [self.t_index, data, 1000.0, 0, 0]
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
            print i[0], i[1], i[2], i[3], i[4]

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

    #Get interest score from ID
    def getIntrestScore(self, ID):
        return self.table[ID][4]

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

        self.plays += 1

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

    def updateInterestScores(self):
        ranks = self.__returnSortedRanks()

        print "DEBUG PRE UPDATE"
        for i in ranks:
            print i
        print "\n"

        for i in range(0, len(ranks)):
            if (i == 0):
                self.table[i][4] = abs(ranks[i][1] - ranks[i+1][1]) * 2.0
            elif(i == (len(ranks) - 1)):
                self.table[i][4] = abs(ranks[i][1] - ranks[i-1][1]) * 2.0
            else:
                self.table[i][4] += abs(ranks[i][1] - ranks[i+1][1])
                self.table[i][4] += abs(ranks[i][1] - ranks[i-1][1])

        print "DEBUG POST UPDATE"
        for i in self.table:
            print i[0], i[2], i[4]
        print "\n"

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

    def __findNMostInteresting(self, n):
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
                print "R1 " + str(r)
                l1 = self.__returnIDFromRandomWeighting(r)
                r = random.uniform(0, total_sum)
                print "R2 " + str(r)
                l2 = self.__returnIDFromRandomWeighting(r)

                print "DEBUG[" + str(count) + "]: " + str(len(pairs))

                check = True
                if (len(pairs) > 0):
                    for i in range(0, len(pairs)): #Is this pairing already in our pairs list?
                        if (((l1 == pairs[i][0]) and (l2 == pairs[i][1])) or ((l2 == pairs[i][0]) and (l1 == pairs[i][1]))):
                            print "CHECK FAILED"
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

    #Choose the n most interesting pairs
    def pickPairs(self, n):

        #Print out ranks
        ranks = self.__returnSortedRanks()

        pairs = []
        #If there have been at least t_index * 10 comparisons
        #   pick the two least played sentences
        #if (self.plays >= self.t_index * 10): #TODO Change so least played happens first
        print "PLAYS " + str(self.plays)
        if (self.plays == 0):
            for i in range(0, n):
                pairs.append(self.__find2LeastPlayed())
                self.table[pairs[i][0]][3] += 1 #Artifically boost plays
                self.table[pairs[i][1]][3] += 1

            for p in pairs: #Reset plays
                self.table[p[0]][3] -= 1
                self.table[p[1]][3] -= 1

        else: #Afterwards, pick pairs based on how many similar neighbours they have
            self.printAll()
            self.updateInterestScores()
            self.printAll()
            print "DEBUG START"
            pairs = self.__findNMostInteresting(n)

            #TODO remove
            print "Pairs:"
            for i in pairs:
                print i
            print ""


        return pairs

    def prune(self):
        #After n plays, each sentence will be able to be pruned if in the
        # bottom n % of the table -- That'll probs be 2nd STDEV
        print "PRUNE"

    #Save a copy of table in the logs dir
    def saveTable(self):
        return True

    #Export a copy of the table after dividing data into seperate bins for analysis
    def exportData(self):
        file = open((str(self.fname) + str(self.w_index) + ".txt"), 'w')
        self.w_index += 1
        for i in range(0, len(self.table)):
            for j in range(0, 4):
                file.write(str(self.table[i][j]) + '\n')
            file.write('\n')
        file.close()
