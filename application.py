import tornado.escape
import tornado.ioloop
import tornado.web
from api.history_handler import HistoryHandler
from api.journey_handler import JourneyHandler
from api.user_handler import UserHandler
from api.version_handler import VersionHandler


application = tornado.web.Application([
    (r"/api/v1.0/version", VersionHandler),
    (r"/api/v1.0/history", HistoryHandler),
    (r"/api/v1.0/history/([\w]+)", HistoryHandler),
    (r"/api/v1.0/user", UserHandler),
    (r"/api/v1.0/user/([\w]+)", UserHandler),
    (r"/api/v1.0/journey", JourneyHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

