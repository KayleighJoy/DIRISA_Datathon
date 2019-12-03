#Class to read in from textfile

import csv
from sklearn.model_selection import train_test_split
import SVM as svm
import RandomForest as rf
import matplotlib.pyplot as plt

class Classify:
    def __init__(self, filename, filename2):
        self.filename = filename
        self.filename2 = filename2
        self.features = list()
        self.labels = list()
        self.X_train = list()
        self.X_test = list()
        self.y_test = list()
        self.y_train = list()
        self.lim = list()
        self.gau = list()
        self.wc = list()
        self.ec = list()
        self.nc = list()
        self.fs = list()
        self.kzn = list()
        self.nw = list()
        self.mpu = list()


    def classifySVM(self):
        self.read_csv()
        self.split_data()
        self.runSVM()
        plt.show()

    def classifyRF(self):
        self.read_csv()
        self.split_data()
        self.runRandomForest()
        plt.show()

    def read_csv(self):
        with open(self.filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(row)
                length = len(row)
                self.features.append(row[1:length])
                temp = []
                temp.append(row[0])
                self.labels.append(temp)
        #print(self.features)
        #print(self.labels)

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.features, self.labels, test_size = 0.25)

    def runSVM(self):
        temp = svm.ClassifySVM(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        plot = temp.svmTrainForMetrics("SVM")
        return plot   
    
    def runRandomForest(self):
        temp = rf.classifyRF(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        plot = temp.trainRfForMetrics("RF")
        return plot  

    def write_csv(self, toWrite):
        with open(self.filename2, mode='w') as writeDS:
            ds_writer = csv.writer(writeDS, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            ds_writer.writerows(toWrite)

    def read_csv_census(self):
        SA_features = []
        with open(self.filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                length = len(row)
                SA_features.append(row)

        for person in SA_features:
            prov = person[0]
            if prov == '1':
                self.wc.append(person)
            elif prov == '2':
                self.ec.append(person)
            elif prov == '3':
                self.nc.append(person)
            elif prov == '4':
                self.fs.append(person)
            elif prov == '5':
                self.kzn.append(person)
            elif prov == '6':
                self.nw.append(person)
            elif prov == '7':
                self.gau.append(person)
            elif prov == '8':
                self.mpu.append(person)
            elif prov == '9':
                self.lim.append(person)
            else:
                print("Error:")
                print(person)

            

    

#path = str(".\DataSets\Mental_Illness_Survey_Matched_Converted.csv")
mainRun = Classify("..\DataSets\CensusData_Cleaned.csv", "")
#mainRun.classifySVM()
mainRun.read_csv_census()
#mainRun.classifyRF()



   

    