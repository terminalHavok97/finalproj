#!/usr/bin/python
#Tom Vaughan - tv15461

from sentencer import Sentencer
from audio import AudioPlayer
import sys
import os

fname = "bin/tta.mp3"
sGen = Sentencer()
ap = AudioPlayer()

for i in range(1,10):
    result = sGen.getSentenceString()
    ap.textToAudio(result, fname)
    ap.playSavedAudio(fname)
