class AudioPlayer:
    try:
        from gtts import gTTS
        from pydub import AudioSegment
        from pydub.playback import play
    except ImportError:
        raise ImportError('<AudioPlayer import error>')
    global gTTS, AudioSegment, play

    def textToAudio(self, t, fname, speed=False):
        tts = gTTS(text=t, lang='en', slow=speed)
        tts.save(fname)

    def playSavedAudio(self, fname):
        a = AudioSegment.from_mp3(fname)
        play(a)
