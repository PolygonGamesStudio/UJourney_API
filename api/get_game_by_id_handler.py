from datetime import date
import tornado


class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = {
            'id': int(id),
            'name': 'Crazy Game',
            'release_date': date.today().isoformat()
        }
        self.write(response)
