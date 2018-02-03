import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "Websocket connected"
        words = ["red", "blue", "green", "yellow"]
        for w in words:
            self.write_message(w);


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
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(3000)
    tornado.ioloop.IOLoop.instance().start()
