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
        print "Testing tts"
        self.textToAudio("Hello I am working")

    def textToAudio(self, t, speed=False):
        tts = gTTS(text=t, lang='en', slow=speed)
        tts.save("bin/tta.wav")

    def playSavedAudio(self, fname):
        return -1
