class Experiment
    try:
        import threading
        from sentence import Sentencer
        from rank import Ranker
        from audio import AudioPlayer
        import time
        import os
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

        #Set exp going
        t_start = time.time()
        self.start(10)
        t_end = time.time()

    #Start experiment, play audio of each pair of sentances and choose which is
    #more normal
    def start(self, itr):
        #For each pairwise comparison
        for i in range(0, itr):
            __clear()
            print "Press 'a' for option 1"
            print "Press 'd' for option 2"
            result = raw_input()

    #Stop experiment
    def stop():

    def __display():

    def __clear(self):
        clear = lambda: os.system('cls')
        clear()
