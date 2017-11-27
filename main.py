#!/usr/bin/python
#Tom Vaughan - tv15461

#from experiment import Experiment

from rank import Ranker
from sentence import Sentencer


#TODO Test
ranker = Ranker()
sGen = Sentencer()

for i in range(0, 10):
    sen = sGen.getSentenceString()
    ranker.addToTable(sen)

for i in range(0, 20):
    ranker.printAll()
    choice = ranker.find2LeastPlayed()
    print "CHOICE: ", choice
    ranker.updateFromComparison(choice[0], choice[1])
    ranker.printAll()



#exp = Experiment()

#TODO Get cmd arguments in????
#TODO Work out how sample sizes and multiple participants will work
