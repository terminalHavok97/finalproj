#!/usr/bin/python
#Tom Vaughan - tv15461

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
        #Send each word of each sentance
        for i in range(0, ranker.t_index):
            sen = ranker.getData(i)
            self.write_message(sen)


        #for w in words:
            #self.write_message(w);


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
