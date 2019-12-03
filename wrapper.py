from classifiers.ReadIn_Data import Classify
from classifiers.SVM import ClassifySVM
import numpy as np

#get number of healthy and ill people per province
def getAllProvinceData():
    dataReader = Classify()
    return dataReader.getAll_prov()

# get average risks
def getCountryPercentage():
    dataReader = Classify()
    return dataReader.country_percentage()

#predict the person's risk 
def predictRisk(education, disabled, unemployed, age, gender, income, mobile, hospital):
    svm = ClassifySVM(0,0,0,0,0,0)
    data = [[education,disabled,unemployed,age,gender,income,mobile,hospital]]
    data = np.asarray(data)
    pred = svm.svmPredictProb(data)
    return pred



