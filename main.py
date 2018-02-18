#!/usr/bin/python
#Tom Vaughan - tv15461

#TODO Work out how sample sizes and multiple participants will work
#TODO Look at pruning out some bad sentences
#TODO Attention trap - Every n sentences, do something weird requiring a 3rd type
# of key press. Could do a fish sentence?
#TODO Add rank element based on a gaussian, so matching isn't just based
# on least played
#TODO Make GUI class for word matching - only eeg needs to be audio only
    #GUI needs to be made for web version, not this program which deals with
    # the server-side program
#TODO JS psych - Could be an option for building the client stuff
#TODO Make sure there's a "how many left" type thing on the client
#TODO If ranker drops poorly performing sentence while a client is
    #still testing on it, on return, drop client's test data for that sentence
#TODO Have logs saved for each client response, init of table, and final results
#TODO Upgrade prune so that it takes note mostly of 3 classes - the best, the worst, and the median
    #Each of these classes can hold a number of sentences

#https://en.wikipedia.org/wiki/Garden_path_sentence#Brain_processing_in_computation

'''TODO
    1. Start client process
    2. Client contacts server, and asks for a set of matches
        a. Server picks from sentences that its most interested in
        b. Server determines matches, and sends those to client
    3. Client recives a set of matches from the server, and runs them in experiment
    4. Client records results of each match, sends those back to server when done
        a. Server takes set of match results, and applies those to their respective
        sentences, updating the rankings between them'''

try:
    import os
    import tornado.web
    import tornado.websocket
    import tornado.httpserver
    import tornado.ioloop
    from rank import Ranker
    from sentence import Sentencer
except ImportError:
    raise ImportError('<Main import error>')

global Sentencer, Ranker, os

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.pairs = []
        self.raw = []

        print "Websocket connected"

        #Get n pairs
        #TODO Upgrade to better version
        self.pairs = ranker.pickPairsNaive(10)

        #Send order
        #No tests for init
        #ID of sen1
        #Data of sen1
        #ID of sen2
        #Data of sen2

        self.write_message(str(10))

        for p in self.pairs:
            self.write_message(str(p[0]))
            self.write_message(' '.join(ranker.getData(p[0])))
            self.write_message(str(p[1]))
            self.write_message(' '.join(ranker.getData(p[1])))
        print "Test data sent\n"

    def on_message(self, msg):
        self.raw.append(int(msg))

    def convertToArray(self):
        l1 = -1
        l2 = -1
        for i in range(0, len(self.raw), 2):
            l1 = self.raw[i]
            l2 = self.raw[i+1]
            r = [l1, l2]
            self.results.append(r)

    def on_close(self):
        print "Websocket destroyed"
        self.results = []
        self.convertToArray()
        ranker.updateNFromComparison(self.results)
        ranker.printAll()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket', WebSocketHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': './templates', 'default_filename': 'index.html'}),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': os.path.join(os.path.dirname("jspsych-6.0.1"), "jspsych.js")
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':

    #Generate sentences and init table
    sGen = Sentencer()
    ranker = Ranker()

    sen = sGen.getNSentences(10)
    ranker.addAllToTable(sen)
    ranker.printAll()

    print "Starting server..."
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(5000)
    print "Listening on port 5000"
    print ""
    tornado.ioloop.IOLoop.instance().start()
