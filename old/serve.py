#!/usr/bin/python

import os
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web as web

from tornado.options import define, options

port = 3000

listeners = []

#http://www.tornadoweb.org/en/stable/guide/templates.html

#https://stackoverflow.com/questions/10438866/message-passing-with-tornado-websockets

public_root = os.path.join(os.path.dirname(__file__), 'public')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message(u"Hello World")

    def on_message(self, message):
        print 'message received %s' % message

    def on_close(self):
      print 'connection closed'

    def check_origin(self, origin):
        return True

handlers = [
    (r'/', MainHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': public_root}),
    (r'/echo', WSHandler),
]

settings = dict(
    debug=True,
    static_path=public_root,
    template_path=public_root
)

app = web.Application(handlers, **settings)

if __name__ == "__main__":
    print "Listening on port: " + str(port)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()


'''class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("templates/index.html")
        #Do I actually need to use any real JS here? Could just make the forms
        #myself and use tornado templates?

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "Opened a new websocket"
        listeners.append(self)
        print listeners

    def on_message(self, message):
        print ("in on_message templates" + message)
        change = message     <script

def make_app():
    return tornado.web.Application([
        (r"/ws", WSHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print "Listening on port: " + str(port)
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()'''
