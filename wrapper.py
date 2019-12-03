from classifiers.ReadIn_Data import Classify

#get number of healthy and ill people per province
def getAllProvinceData():
    dataReader = Classify()
    return dataReader.getAll_prov()

# get average risks
def getCountryPercentage():
    dataReader = Classify()
    return dataReader.country_percentage()

def getHeatMapInfo():
    dataReader = Classify()
    return dataReader.display_heatmap()

print(getHeatMapInfo())

