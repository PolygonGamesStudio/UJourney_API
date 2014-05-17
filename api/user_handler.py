import tornado
from database.MongoDBORM import MongoORM as ORM


class UserHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        orm = ORM("Journey")

        if user_id:
            result = orm.select("user", {"user.user_id": user_id})
            self.write(result)
        else:
            self.write({})
        del orm

    def post(self):
        orm = ORM("Journey")
        try:
            data = tornado.escape.json_decode(self.request.body)
            orm.insert(data, "user")
            self.write({"status": "ok"})
        except ValueError:
            self.write({
                "status_code": "417",
                 "status_txt": "Invalid POST request, check the data.",
                 "status": "fail"
            })
        del orm
