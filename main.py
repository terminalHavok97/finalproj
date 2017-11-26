#!/usr/bin/python
#Tom Vaughan - tv15461

from sentence import Sentencer
from rank import Ranker
from audio import AudioPlayer

import threading as t
import sys
import os

fname = "bin/tta.mp3"
sGen = Sentencer()
ranker = Ranker()

for i in range(0,3):
    s = sGen.getSentenceString()
    ranker.addToTable(s)

#0 wins against 2
ranker.printAll()
ranker.updateFromComparison(0, 1)
ranker.printAll()
ranker.updateFromComparison(0, 2)
ranker.printAll()
ranker.updateFromComparison(1, 0)
ranker.printAll()
