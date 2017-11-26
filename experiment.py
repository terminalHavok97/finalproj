class Experiment
    try:
        import threading
        from sentence import Sentencer
        from rank import Ranker
        from audio import AudioPlayer
        import time
    except ImportError:
        raise ImportError('<Experiment import error>')
    global threading, Sentencer, Ranker, AudioPlayer, time

    #Make table of sentances, initialise everything
    def __init__(self, number):
        #Inits
        self.fname = "bin/tta.mp3"
        self.sGen = Sentencer()
        self.ranker = Ranker()
        self.ap = AudioPlayer()

        #Gen arg number of sentences
        for i in range(0, number):
            sen = self.sGen.getSentenceString()
            self.ranker.addToTable(sen)

        self.start()

    #Start experiment, play audio of each pair of sentances and choose which is
    #more normal
    def start():

    #Stop experiment
    def stop():

    def __display():
