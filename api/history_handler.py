import json
from database.MongoDBORM import MongoORM as ORM
import tornado


class HistoryHandler(tornado.web.RequestHandler):

    def post(self):
        """
        Добавления в БД, о посищении места

        @return: ответ сервера о статусе добавления данных
        """
        orm = ORM("Journey")
        #  TODO: проверка json и ответ ошибкой из доков
        data = tornado.escape.json_decode(self.request.body)
        orm.insert(data, "history")

        del orm
        self.write({"status": "ok"})

    def get(self):
        """
        Получения списка мест в кторорых был пользователь

        @param user_id: поле по которому идёт выборка из базы

        @return: ответ сервера о статусе добавления данных
        """
        data = tornado.escape.json_decode(self.request.body)
        orm = ORM("Journey")

        if data['user_id']:
            result = orm.select("history", {"user.user_id": data['user_id']})
            self.write(json.dumps(list(result)))
        else:
            self.write({})
        del orm

    def delete(self):
        """
        Удаление экземпляра истории из БД

        @param user_id: поле по которому идёт выборка из базы
        @param token: пока не используется

        @return: ответ сервера о статусе добавления данных
        """
        data = tornado.escape.json_decode(self.request.body)
        orm = ORM("Journey")

        if data['place_id'].isdigit():
            orm.delete("history", {"id": int(data['place_id'])})
            self.write({"status": "ok"})
        else:
            self.write({
                "status_code": "411",
                "status_txt": "Invalid DELETE request, check the data.",
                "status": "fail"
            })
        del orm




