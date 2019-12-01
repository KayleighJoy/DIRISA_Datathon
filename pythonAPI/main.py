import testResource
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class getAge(Resource):
    def get(self, year, month, day):
        return {'data': testResource.calcAge(year,month,day)}

api.add_resource(getAge, '/calcAge/<year>/<month>/<day>')

if __name__ == '__main__':
     app.run()