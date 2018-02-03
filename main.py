#!/usr/bin/python
#Tom Vaughan - tv15461

#TODO Work out how sample sizes and multiple participants will work
#TODO Look at pruning out some bad sentences
#TODO Attention trap - Every n sentances, do something weird requiring a 3rd type
# of key press. Could do a fish sentance?
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
        sentances, updating the rankings between them'''

try:
    import tornado.web
    import tornado.websocket
    import tornado.httpserver
    import tornado.ioloop

    from rank import Ranker
    from sentence import Sentencer

except ImportError:
    raise ImportError('<Main import error>')

global Sentencer, Ranker

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "Websocket connected"

        #Send order
        #ID of sen1
        #Data of sen1
        #ID of sen2
        #Data of sen2

        #TODO TEST CASE
        self.write_message(0)
        self.write_message(ranker.getData(0))
        self.write_message(1)
        self.write_message(ranker.getData(1))
        self.write_message(2)
        self.write_message(ranker.getData(2))
        self.write_message(3)
        self.write_message(ranker.getData(3))

        #Send each word of each sentance
        #for i in range(0, ranker.t_index):
        #    sen = ranker.getData(i)
        #    self.write_message(sen)

    def on_message(self, message):
        #self.write_message(u"Your message was: " + message)
        results = message
        print "Results from client: " + message

    def on_close(self):
        print "Websocket destroyed"


class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/websocket', WebSocketHandler)
        ]

        settings = {
            'template_path': 'templates'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    #Generate sentances and init table
    sGen = Sentencer()
    ranker = Ranker()

    for i in range(0, 10):
        sen = sGen.getSentenceString()
        ranker.addToTable(sen)
    ranker.printAll()

    print "Starting server..."
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(3000)
    print "Listening on port 3000"
    print ""
    tornado.ioloop.IOLoop.instance().start()
