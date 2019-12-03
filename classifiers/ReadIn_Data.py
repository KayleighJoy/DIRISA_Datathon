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

    def classifySVM(self):
        self.read_csv()
        self.split_data()
        self.runSVM()
        plt.show()

    def classifyRF(self):
        self.read_csv()
        self.split_data()
        self.runSVM()
        plt.show()

    def read_csv(self):
        with open(self.filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(row)
                length = len(row)
                temp2 = []
                temp2.append(row[1])
                temp2.append(row[6])
                self.features.append(temp2)
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

    

path = str(".\DataSets\Mental_Illness_Survey_Matched_Converted.csv")
mainRun = Classify("..\DataSets\Mental_Illness_Survey_Converted_Sequential.csv", "")
mainRun.classifySVM()
#mainRun.classifyRF()



   

    