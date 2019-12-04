from flask import Flask, request
from flask_restful import Resource, Api
import wrapper

app = Flask(__name__)
api = Api(app)

class getAllProvince(Resource):
    def get(self):
        provData = wrapper.getAllProvinceData()
        return {'Western Cape': provData[0], 'Eastern Cape': provData[1], 'Northern Cape': provData[2], 'Free State': provData[3], 'KwaZulu Natal': provData[4], 'North West': provData[5], 'Gauteng': provData[6], 'Mpumalanga': provData[7], 'Limpopo': provData[8],}

class getCountryPercentage(Resource):
    def get(self):
        riskAve = wrapper.getCountryPercentage()
        return{"Country Risk": riskAve}

class getCountryWeightedPercentage(Resource):
    def get(self):
        risk = wrapper.getCountryWeightedPercentage()
        return {"CountryRisk": risk}

class predictRisk(Resource):
    def get(self, education, disabled, unemployed, age, gender, income, mobile, hospital):
        riskAve = wrapper.predictRisk(education, disabled, unemployed, age, gender, income, mobile, hospital)
        print(riskAve[0][0])
        if riskAve[0][0]>riskAve[0][1]:
            return {'status': 'At Risk', 'prob': riskAve[0][0]}
        else:
            return {'status': 'Not At Risk', 'prob': riskAve[0][1]}

class getHeatMap(Resource):
    def get(self):
        provData = wrapper.getHeatMapInfo()
        return {'Western Cape': provData[0], 'Eastern Cape': provData[1], 'Northern Cape': provData[2], 'Free State': provData[3], 'KwaZulu Natal': provData[4], 'North West': provData[5], 'Gauteng': provData[6], 'Mpumalanga': provData[7], 'Limpopo': provData[8],}


api.add_resource(getAllProvince, '/getAllProvinceData')
api.add_resource(getCountryPercentage, '/getCountryRisk')
api.add_resource(getHeatMap, '/getHeatMapData')
api.add_resource(predictRisk, '/predict/<education>/<disabled>/<unemployed>/<age>/<gender>/<income>/<mobile>/<hospital>')
api.add_resource(getCountryWeightedPercentage, '/countryWeightedRisk')

if __name__ == '__main__':
     app.run()