import tornado.escape
import tornado.ioloop
import tornado.web
from api.get_game_by_id_handler import GetGameByIdHandler
from api.version_handler import VersionHandler


application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

