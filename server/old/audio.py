class AudioPlayer:
    try:
        from gtts import gTTS
        import pyglet
    except ImportError:
        raise ImportError('<AudioPlayer import error>')
    global gTTS, pyglet

    #Convert text into mp3 audio - speed flag sets the speech speed
    def textToAudio(self, t, fname, speed=False):
        tts = gTTS(text=t, lang='en', slow=speed)
        tts.save(fname)

    #Play a saved mp3
    def playSavedAudio(self, fname):
        sound = pyglet.media.load(fname, streaming=False)
        sound.play()
        return 1
        #pyglet.app.run()
