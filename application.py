import tornado.escape
import tornado.ioloop
import tornado.web
from api.history_handler import HistoryHandler
from api.version_handler import VersionHandler


application = tornado.web.Application([
    (r"/version", VersionHandler),
    (r"/history", HistoryHandler),
    (r"/history/([\w]+)", HistoryHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

