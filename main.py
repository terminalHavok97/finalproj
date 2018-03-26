#!/usr/bin/python
#Tom Vaughan - tv15461

#TODO Look at pruning out some bad sentences
#TODO Add rank element based on a gaussian, so matching isn't just based
# on least played
#TODO Make GUI class for word matching - only eeg needs to be audio only
    #GUI needs to be made for web version, not this program which deals with
    # the server-side program
#TODO Make sure there's a "how many left" type thing on the client
#TODO If ranker drops poorly performing sentence while a client is
    #still testing on it, on return, drop client's test data for that sentence
#TODO Have logs saved for each client response, init of table, and final results

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
    from random import shuffle
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
        self.pairs = ranker.pickPairs(60)
        fish_length = int(len(self.pairs) * 0.1)
        fish = sGen.fishify(fish_length)
        self.pairs.extend(fish)
        l = len(self.pairs)
        shuffle(self.pairs)

        #Send order:
        #No tests for init
        #ID of sen1
        #Data of sen1
        #ID of sen2
        #Data of sen2

        self.write_message(str(l))

        index = 0
        for p in self.pairs:
            if p[0] == -1: #Fish case
                self.write_message(str(p[0]))
                self.write_message(' '.join(p[1]))
                self.write_message(str(p[2]))
                self.write_message(' '.join(p[3]))
                #print "[" + str(index) + "]: " + (' '.join(p[1])) + " ==> F"
                #print "[" + str(index) + "]: " + (' '.join(p[3])) + " ==> F"
                #print ""
                index += 1
            else:
                self.write_message(str(p[0]))
                self.write_message(' '.join(ranker.getData(p[0])))
                self.write_message(str(p[1]))
                self.write_message(' '.join(ranker.getData(p[1])))
                #print "[" + str(index) + "]: " + (' '.join(ranker.getData(p[0])))
                #print "[" + str(index) + "]: " + (' '.join(ranker.getData(p[1])))
                #print ""
                index += 1
        print "Test data sent\n"

    def on_message(self, msg):
        self.raw.append(int(msg))
        #print msg

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
        print "Table updated\n"
        ranker.printAll()
        ranker.exportData()
        #ranker.exportAsGraph()

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

    #sen = sGen.getNSentences(20)
    #ranker.addAllToTable(sen)
    ranker.importTable("test/table0.txt")
    ranker.printAll()
    ranker.find2RandomRanked()
    #ranker.exportAsGraph()

    print "Starting server..."
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(5000)
    print "Listening on port 5000"
    print ""
    tornado.ioloop.IOLoop.instance().start()
