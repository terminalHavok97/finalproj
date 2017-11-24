from gtts import gTTS
import os
import vlc

tts = gTTS(text='Hello fellow human how are you?', lang='en')
tts.save("good.mp3")

p = vlc.MediaPlayer("good.mp3")
p.play()
