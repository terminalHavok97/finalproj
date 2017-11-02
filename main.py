#Tom Vaughan - tv15461

#prelim experiment
#import word lists
#build them so they're grammatically good bois
#blank white/black screen
#play audio of sentance 1, then sentance 2
#buttons to choose which is better
#update elo rank

#Text to speech test

from gtts import gTTS
import os
import vlc

tts = gTTS(text='Hello fellow human how are you?', lang='en')
tts.save("good.mp3")

p = vlc.MediaPlayer("good.mp3")
p.play()
