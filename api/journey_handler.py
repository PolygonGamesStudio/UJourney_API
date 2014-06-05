import json
from database.MongoDBORM import MongoORM as ORM
import tornado


class JourneyHandler(tornado.web.RequestHandler):

    def get(self):
        try:
            time = self.get_argument('time')
            cost = self.get_argument('cost')
            category_id = self.get_argument('category_id', None)
            conditions_dict = {
                "time": {"$lt": int(time)},
                "cost": {"$lt": int(cost)}
            }
            if category_id is not None:
                conditions_dict["category_id"] = int(category_id)

            orm = ORM("ujdb")
            result = orm.select("places", conditions_dict)
            self.write(json.dumps(list(result)))
            del orm
        except ValueError:
            raise tornado.web.HTTPError(400, u'numbers expected')


