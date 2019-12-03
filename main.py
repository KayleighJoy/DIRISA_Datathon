from flask import Flask, request
from flask_restful import Resource, Api
import wrapper

app = Flask(__name__)
api = Api(app)

class getAllProvince(Resource):
    def get(self):
        provData = wrapper.getAllProvinceData()
        return {'Western Cape': provData[0], 'Eastern Cape': provData[1], 'Northern Cape': provData[2], 'Free State': provData[3], 'KwaZulu Natal': provData[4], 'North West': provData[5], 'Gauteng': provData[6], 'Mpumalanga': provData[7], 'Limpopo': provData[8],}

api.add_resource(getAllProvince, '/getAllProvinceData')

if __name__ == '__main__':
     app.run()