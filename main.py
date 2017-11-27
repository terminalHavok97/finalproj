#!/usr/bin/python
#Tom Vaughan - tv15461

from experiment import Experiment

from rank import Ranker


#TODO Test
ranker = Ranker()
sGen = Sentencer()

for i in range(0, 10):
    sen = sGen.getSentenceString()
    ranker.addToTable(sen)


#exp = Experiment()

#TODO Get cmd arguments in?
#TODO Work out how sample sizes and multiple participants will work
