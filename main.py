#!/usr/bin/python
#Tom Vaughan - tv15461

from sentencer import Sentencer
from audio import AudioPlayer
import sys
import os

fname = "bin/tta.mp3"

#ap = AudioPlayer()
#ap.textToAudio("Oi Oi Savaloy", fname)
#ap.playSavedAudio(fname)


sGen = Sentencer()

for i in range(1,10):
    result = sGen.getSentenceString()
    print result
