#!/usr/bin/python
#Tom Vaughan - tv15461
try:
    from experiment import Experiment
    import time
except ImportError:
    raise ImportError('<Main import error>')

exp = Experiment(3, 5, 10)

#TODO Work out how sample sizes and multiple participants will work
#TODO Look at pruning out some bad sentences
#TODO Attention trap - Every n sentances, do something weird requiring a 3rd type
# of key press. Could do a fish sentance?
#TODO Look into web page serving - probably Javascript of psypy
#TODO Simple message passing between python serving and JS client
#TODO Add rank element based on a gaussian, so matching isn't just based
# on least played
#TODO Make GUI class for word matching - only eeg needs to be audio only
