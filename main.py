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

sGen = Sentencer()
ranker = Ranker()

for i in range(0, 10):
    sen = sGen.getSentenceString()
    ranker.addToTable(sen)
ranker.printAll()
