from classifiers.ReadIn_Data import Classify

def getAllProvinceData():
    dataReader = Classify()
    return dataReader.getAll_prov()
