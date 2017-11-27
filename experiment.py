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
    global threading, Sentencer, Ranker, AudioPlayer, time, os

    #Make table of sentances, initialise everything
    #@n is number of sentances to create
    #@t is timeout per question
    #@i is the number of comparison tests to run
    def __init__(self, n=10, t=5, i=20):
        #Inits
        self.fname1 = "bin/tta1.mp3"
        self.fname2 = "bin/tta2.mp3"
        self.q_time = t
        self.number = n
        self.itr = i
        self.sGen = Sentencer()
        self.ranker = Ranker()
        self.ap = AudioPlayer()

        #Gen arg number of sentences
        for i in range(0, self.number):
            sen = self.sGen.getSentenceString()
            self.ranker.addToTable(sen)

        #Set exp going
        runtime_start = time.time()
        for j in range(0, self.itr):
            #Decide which 2 sentances have been played least and pick them
            data = self.ranker.find2LeastPlayed()
            data1 = self.ranker.getData(data[0])
            data2 = self.ranker.getData(data[1])
            #Run choice between 2 sentances
            result = self.run(data1, data2)
            print "EXP: ", j, " = ", result

        runtime_end = time.time()
        runtime = runtime_end - runtime_start
        print ""
        print "Runtime: ", runtime

        ranker.printAll()

    #Play a single comparison of the experiment
    def run(self, data1, data2):
        self.__clear()
        print "Please listen to both sentances"
        print "Decide which one sounds MORE normal than the other"
        print "You have 5 seconds to decide"
        print ""
        self.ap.textToAudio(data1, self.fname1)
        self.ap.textToAudio(data2, self.fname2)
        self.ap.playSavedAudio(self.fname1)
        self.ap.playSavedAudio(self.fname2)
        print "Press 'a' for option 1"
        print "Press 'd' for option 2"
        q_start = time.time()
        while time.time() < q_start + self.q_time:
            result = raw_input()
            if result == 'a':
                return 1
            else:
                return 2
        print "TIMEOUT! Next question"
        return 0

    def __display():
        return -1

    #Clear console
    def __clear(self):
        clear = lambda: os.system('clear')
        clear()
