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
    def __init__(self):
        self.start()

    #Start experiment, play audio of each pair of sentances and choose which is
    #more normal
    def start():

    #Stop experiment
    def stop():

    def display():
