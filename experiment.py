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
    def __init__(self):
        #Inits
        self.fname = "bin/tta.mp3"
        self.q_time = 5
        self.itr = 10
        self.sGen = Sentencer()
        self.ranker = Ranker()
        self.ap = AudioPlayer()

        #Gen arg number of sentences
        for i in range(0, number):
            sen = self.sGen.getSentenceString()
            self.ranker.addToTable(sen)

        #Set exp going
        total_start = time.time()
        self.start(10)
        total_end = time.time()
        total_time = total_start - total_end

    #Start experiment, play audio of each pair of sentances and choose which is
    #more normal
    def start(self, itr):
        #For each pairwise comparison
        for i in range(0, itr):
            self.__clear()
            print "Press 'a' for option 1"
            print "Press 'd' for option 2"
            q_start = time.time()
            while time.time() < q_start + self.q_time:
                result = raw_input()
                if result == 'a':
                    ranker.updateFromComparison()


    #Stop experiment
    def stop():

    def __display():

    def __clear(self):
        clear = lambda: os.system('cls')
        clear()
