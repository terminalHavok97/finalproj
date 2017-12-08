class Experiment:
    try:
        from sentence import Sentencer
        from rank import Ranker
        from audio import AudioPlayer
        from gui import GUI
        import time
        import os
        import sys
        import thread
        import threading
        import Tkinter as tk
    except ImportError:
        raise ImportError('<Experiment import error>')
    global Sentencer, Ranker, AudioPlayer, GUI, time, os, sys, thread, threading, tk

    #Make table of sentances, initialise everything
    #@n is number of sentances to create
    #@t is timeout per question
    #@i is the number of comparison tests to run
    def __init__(self, n=10, t=5, i=20):
        #Inits
        self.fname1 = 'bin/tta1.mp3'
        self.fname2 = 'bin/tta2.mp3'
        self.q_time = t
        self.number = n
        self.itr = i
        self.sGen = Sentencer()
        self.ranker = Ranker()
        self.ap = AudioPlayer()
        self.gui = GUI()

        root = tk.Tk()
        self.gui.setupWindow(root)
        self.gui.updateText(root, "Hello")
        time.sleep(1)
        self.gui.updateText(root, "Hello")
        root.mainloop()



        '''
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
            time.sleep(1) #Just to ensure audio isn't skipped through too fast
            if result == 1:
                self.ranker.updateFromComparison(data[0], data[1])
            elif result == 2:
                self.ranker.updateFromComparison(data[1], data[0])

        runtime_end = time.time()
        runtime = runtime_end - runtime_start
        print ""
        print "Runtime: ", runtime

        self.ranker.printAll()
        '''

    #Get choice from user
    def __raw_input_with_timeout(self, timeout):
        timer = threading.Timer(timeout, thread.interrupt_main)
        result = -1
        try:
            timer.start()
            result = raw_input()
        except KeyboardInterrupt:
            pass
        timer.cancel()
        return result


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
        time.sleep(2) #So audio doesn't overlap
        self.ap.playSavedAudio(self.fname2)
        print "Press 'a' for option 1"
        print "Press 'd' for option 2"
        q_start = time.time()

        result = self.__raw_input_with_timeout(self.q_time)

        if result == 'a':
            return 1
        elif result == 'd':
            return 2
        elif result == -1:
            print "TIMEOUT! Next question"
            raw_input("Press Enter to continue...")
            return 0
        else:
            print "Error - Incorrect selection"
            raw_input("Press Enter to continue...")
            return 0

    #Clear console
    def __clear(self):
        clear = lambda: os.system('clear')
        clear()
