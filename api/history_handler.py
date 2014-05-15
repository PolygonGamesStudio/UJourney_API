from database.MongoDBORM import MongoORM as ORM
import tornado


class HistoryHandler(tornado.web.RequestHandler):
    def post(self):
        orm = ORM("test")

        data = tornado.escape.json_decode(self.request.body)
        orm.insert(data, "test")

        del orm

