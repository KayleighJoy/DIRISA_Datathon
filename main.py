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
        print(risk)
        return {"CountryRisk": risk}

class predictRisk(Resource):
    def get(self, education, disabled, unemployed, age, gender, income, mobile, hospital):
        riskAve = wrapper.predictRisk(education, disabled, unemployed, age, gender, income, mobile, hospital)
        print(riskAve[0][0])
        return {'status': 'At Risk', 'prob': riskAve[0][0]}

class getHeatMap(Resource):
    def get(self):
        provData = wrapper.getHeatMapInfo()
        return {'Western Cape': str(provData[0][0])+'-'+str(provData[0][1])+'-'+str(provData[0][2])+'-'+str(provData[0][3])+'-'+str(provData[0][4]), 
        'Eastern Cape': str(provData[1][0])+'-'+str(provData[1][1])+'-'+str(provData[1][2])+'-'+str(provData[1][3])+'-'+str(provData[1][4]), 
        'Northern Cape': str(provData[2][0])+'-'+str(provData[2][1])+'-'+str(provData[2][2])+'-'+str(provData[2][3])+'-'+str(provData[2][4]), 
        'Free State': str(provData[3][0])+'-'+str(provData[3][1])+'-'+str(provData[3][2])+'-'+str(provData[3][3])+'-'+str(provData[3][4]), 
        'KwaZulu Natal': str(provData[4][0])+'-'+str(provData[4][1])+'-'+str(provData[4][2])+'-'+str(provData[4][3])+'-'+str(provData[4][4]), 
        'North West': str(provData[5][0])+'-'+str(provData[5][1])+'-'+str(provData[5][2])+'-'+str(provData[5][3])+'-'+str(provData[5][4]), 
        'Gauteng': str(provData[6][0])+'-'+str(provData[6][1])+'-'+str(provData[6][2])+'-'+str(provData[6][3])+'-'+str(provData[6][4]), 
        'Mpumalanga': str(provData[7][0])+'-'+str(provData[7][1])+'-'+str(provData[7][2])+'-'+str(provData[7][3])+'-'+str(provData[7][4]), 
        'Limpopo': str(provData[8][0])+'-'+str(provData[8][1])+'-'+str(provData[8][2])+'-'+str(provData[8][3])+'-'+str(provData[8][4])}


api.add_resource(getAllProvince, '/getAllProvinceData')
api.add_resource(getCountryPercentage, '/getCountryRisk')
api.add_resource(getHeatMap, '/getHeatMapData')
api.add_resource(predictRisk, '/predict/<education>/<disabled>/<unemployed>/<age>/<gender>/<income>/<mobile>/<hospital>')
api.add_resource(getCountryWeightedPercentage, '/countryWeightedRisk')

if __name__ == '__main__':
     app.run()