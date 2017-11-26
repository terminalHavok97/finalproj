#!/usr/bin/python
#Tom Vaughan - tv15461

from sentence import Sentencer
from rank import Ranker

from audio import AudioPlayer
import sys
import os

fname = "bin/tta.mp3"
sGen = Sentencer()
ranker = Ranker()

for i in range(0,10):
    s = sGen.getSentenceString()
    ranker.addToTable(s)

ranker.printAll()
