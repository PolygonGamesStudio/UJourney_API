from datetime import date
import tornado


class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = {
            'version': '0.0.1',
            'last_build':  date.today().isoformat()
        }
        self.write(response)
