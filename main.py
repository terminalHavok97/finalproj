#!/usr/bin/python
#Tom Vaughan - tv15461

from sentencer import Sentencer

sGen = Sentencer()
for i in range(1, 200):
    print i, sGen.giveSentence()
