import os
from tornado import ioloop,web
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId

MONGODB_DB_URL = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'snap-lighting'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]

class IndexHandler(web.RequestHandler):
  def get(self):
    self.write("Hello World!!")

class LightsHandler(web.RequestHandler):
  def get(self):
    lights = db.lights.find()
    self.set_header("Content-Type", "application/json")
    self.write(json.dumps(list(lights),default=json_util.default))

settings = {
  "template_path": os.path.join(os.path.dirname(__file__), "templates"),
  "static_path": os.path.join(os.path.dirname(__file__), "static"),
  "debug": True
}

application = web.Application([
  (r'/', IndexHandler),
  (r'/index', IndexHandler),
  (r'/api/v1/lights',LightsHandler),
  (r'/bower_components/(.*)', web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "bower_components")})
],**settings)

if __name__ == "__main__":
  application.listen(8888)
  ioloop.IOLoop.instance().start()
