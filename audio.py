'''
from gtts import gTTS
import os
import vlc

tts = gTTS(text='Hello fellow human how are you?', lang='en')
tts.save("good.mp3")

p = vlc.MediaPlayer("good.mp3")
p.play()
'''
class AudioPlayer:
    try:
        import pyaudio
        from gtts import gTTS
        import wave
        import sys
    except ImportError:
        raise ImportError('<AudioPlayer import error>')
    global pyaudio, gTTS, wave, sys

    def __init__(self):
        #self.pya = pyaudio.PyAudio()
        print "All good"

    def textToAudio(self, text):
        return -1
    def playSavedAudio(self, fname):
        return -1
