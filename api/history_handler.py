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
        try:
            data = tornado.escape.json_decode(self.request.body)
            orm.insert(data, "history")
            self.write({"status": "ok"})
        except ValueError:
            self.write({
                "status_code": "417",
                 "status_txt": "Invalid POST request, check the data.",
                 "status": "fail"
            })
        del orm

    def get(self, user_id):
        """
        Получения списка мест в кторорых был пользователь

        @param user_id: уникальный идентификатор пользователя
        @param place_id: уникальный идентификатор места

        @return: ответ сервера о статусе добаввления данных
        """
        orm = ORM("Journey")
        place_id = self.get_argument("place_id", "")

        if user_id:
            if place_id:
                result = orm.select("history", {"user.user_id": user_id, "place.place_id": place_id})
            else:
                result = orm.select("history", {"user.user_id": user_id})
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

        # TODO: сравнение входного массива ключей с требуемым
        # a = [1,2,3]
        # b = [3,2,1,4]
        # set(a).issubset(set(b))

        try:
            data = tornado.escape.json_decode(self.request.body)
        except ValueError:
            data = {}
        orm = ORM("Journey")

        if data.get('place_id', '').isdigit():
            orm.delete("history", {"id": int(data['place_id'])})
            self.write({"status": "ok"})
        else:
            self.write({
                "status_code": "411",
                "status_txt": "Invalid DELETE request, check the data.",
                "status": "fail"
            })
        del orm