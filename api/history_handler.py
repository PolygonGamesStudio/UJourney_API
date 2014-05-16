import json
from database.MongoDBORM import MongoORM as ORM
import tornado


class HistoryHandler(tornado.web.RequestHandler):

    def post(self):
        """
        Добавления в БД, о посищении места

        @return: ответ сервера о статусе добаввления данных
        """
        orm = ORM("Journey")
        #  TODO: проверка json и ответ ошибкой из доков
        data = tornado.escape.json_decode(self.request.body)
        orm.insert(data, "history")

        del orm
        self.write({"status": "ok"})

    def get(self, user_id):
        """
        Получения списка мест в кторорых был пользователь

        @param user_id: поле по которому идёт выборка из базы

        @return: ответ сервера о статусе добаввления данных
        """
        orm = ORM("Journey")

        result = orm.select("history", {"user.user_id": user_id})

        del orm
        self.write(json.dumps(list(result)))


