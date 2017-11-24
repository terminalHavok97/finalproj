#!/usr/bin/python
#Tom Vaughan - tv15461

'''
from gtts import gTTS
import os
import vlc

tts = gTTS(text='Hello fellow human how are you?', lang='en')
tts.save("good.mp3")

p = vlc.MediaPlayer("good.mp3")
p.play()
'''

def readWords(fname):
    with open(fname) as f:
        words = f.readlines()
    words = [x.strip() for x in words]
    return words

#Read in nouns
nouns      = readWords("assets/nouns.txt")
verbs      = readWords("assets/verbs.txt")
adjectives = readWords("assets/adjectives.txt")
