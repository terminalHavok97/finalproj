#!/usr/bin/python
#Tom Vaughan - tv15461
try:
    from experiment import Experiment
except ImportError:
    raise ImportError('<Main import error>')

exp = Experiment(3, 5, 10)

#TODO Work out how sample sizes and multiple participants will work
#TODO Look at pruning out some bad sentences
#TODO Attention trap - Every n sentances, do something weird requiring a 3rd type
# of key press. Could do a fish sentance?
#TODO Look into web page serving - probably Javascript or psypy
#TODO Simple message passing between python serving and JS client
#TODO Add rank element based on a gaussian, so matching isn't just based
# on least played
#TODO Make GUI class for word matching - only eeg needs to be audio only
    #GUI needs to be made for web version, not this program which deals with
    # the server-side program
#TODO JS psych - Could be an option for building the client stuff
#TODO Make sure there's a "how many left" type thing on the client

#https://en.wikipedia.org/wiki/Garden_path_sentence#Brain_processing_in_computation

'''TODO
    1. Start client process
    2. Client contacts server, and asks for a set of matches
        a. Server picks from sentances that its most interested in
        b. Server determines matches, and sends those to client
    3. Client recives a set of matches from the server, and runs them in experiment
    4. Client records results of each match, sends those back to server when done
        a. Server takes set of match results, and applies those to their respective
        sentances, updating the rankings between them
