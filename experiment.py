class Experiment:
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
    def __init__(self, n=10, t=5):
        #Inits
        self.fname1 = "bin/tta1.mp3"
        self.fname2 = "bin/tta2.mp3"
        self.q_time = t
        self.number = n
        self.sGen = Sentencer()
        self.ranker = Ranker()
        self.ap = AudioPlayer()

        #Gen arg number of sentences
        for i in range(0, self.number):
            sen = self.sGen.getSentenceString()
            self.ranker.addToTable(sen)

        #Set exp going
        total_start = time.time()
        self.start(10)
        total_end = time.time()
        total_time = total_start - total_end
        print total_time

        #Set exp going
        runtime_start = time.time()
        for i in range(0, self.itr):
            data1 = ranker.getData(i)

            result = run(data1, data2)

        runtime_end = time.time()
        runtime = runtime_end - runtime_start
        print "Runtime: ", runtime


    #Play a single comparison of the experiment
    def run(self, data1, data2):
        self.__clear()
        print "Please listen to both sentances"
        print "Decide which one sounds MORE normal than the other"
        print ""
        au.textToAudio(data1, self.fname1)
        au.textToAudio(data2, self.fname2)
        au.playSavedAudio(self.fname1)
        au.playSavedAudio(self.fname2)
        print "Press 'a' for option 1"
        print "Press 'd' for option 2"
        q_start = time.time()
        while time.time() < q_start + self.q_time:
            result = raw_input()
            if result == 'a':
                return 1
            else:
                return 2
        return 0



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

    def __display():
        return -1

    #Clear console
    def __clear(self):
        clear = lambda: os.system('cls')
        clear()