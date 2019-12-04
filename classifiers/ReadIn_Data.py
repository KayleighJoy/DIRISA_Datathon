#Class to read in from textfile

import csv
from sklearn.model_selection import train_test_split
import classifiers.SVM as svm
import classifiers.RandomForest as rf
import matplotlib.pyplot as plt
import numpy as np

class Classify:
    def __init__(self):
        self.filename = ".\DataSets\CensusData_Cleaned.csv"
        self.filename2 = ""
        self.features = list()
        self.labels = list()
        self.X_train = list()
        self.X_test = list()
        self.y_test = list()
        self.y_train = list()
        self.all_prov = list()
        self.wc = []
        self.ec = []
        self.nc = []
        self.fs = []
        self.kzn = []
        self.nw = []
        self.gau = []
        self.mpu = []
        self.lim = []
        self.SA_features = []


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
        with open(".\DataSets\Mental_Binary_Labels_More.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                length = len(row)
                self.features.append(row[1:length])
                temp = []
                temp.append(row[0])
                self.labels.append(temp)
        #print(self.features)
        #print(self.labels)

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.features, self.labels, test_size = 0.20)

    def runSVM(self):
        temp = svm.ClassifySVM(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        plot = temp.svmTrainForMetrics("SVM")
        return plot 

    def getAll_prov(self):
        self.read_csv()
        self.split_data()
        self.read_csv_census()
        return self.provinces_percentage_svm()

    def getAll_prov_RF(self):
        self.read_csv()
        self.split_data()
        self.read_csv_census()
        self.provinces_percentage_rf()
        self.country_percentage_rf()
    
    def runRandomForest(self):
        temp = rf.classifyRF(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        plot = temp.trainRfForMetrics("RF")
        return plot  

    def country_percentage(self):
        self.read_csv()
        self.split_data()
        self.read_csv_census()
        temp = svm.ClassifySVM(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        pred = temp.svmTrain(self.SA_features)
        return self.one_province(pred)

    def country_percentage_weighted(self):
        self.read_csv()
        self.split_data()
        self.read_csv_census()
        expectedWeight = self.provinces_percentage_svm()
        self.split_provinces(self.SA_features)
        ratioWC = len(self.wc)/len(self.SA_features)
        ratioEC = len(self.ec)/len(self.SA_features)
        ratioNC = len(self.nc)/len(self.SA_features)
        ratioFS = len(self.fs)/len(self.SA_features)
        ratioKZN = len(self.kzn)/len(self.SA_features)
        ratioNW = len(self.nw)/len(self.SA_features)
        ratioGau = len(self.gau)/len(self.SA_features)
        ratioMpu = len(self.mpu)/len(self.SA_features)
        ratioLim = len(self.lim)/len(self.SA_features)

        real_ratioWC = 5822734/51770561
        real_ratioEC = 6562053/51770561
        real_ratioNC = 1145861/51770561
        real_ratioFS = 2745590/51770561
        real_ratioKZN = 10267300/51770561
        real_ratioNW = 3509953/51770561
        real_ratioGau = 12272263/51770561
        real_ratioMpu = 4039939/51770561
        real_ratioLim = 5404868/51770561

        print(str(ratioWC) + ":" + str(real_ratioWC))
        print(str(ratioEC) + ":" + str(real_ratioEC))
        print(str(ratioNC) + ":" + str(real_ratioNC))
        print(str(ratioFS) + ":" + str(real_ratioFS))
        print(str(ratioKZN) + ":" + str(real_ratioKZN))
        print(str(ratioNW) + ":" + str(real_ratioNW))
        print(str(ratioGau) + ":" + str(real_ratioGau))
        print(str(ratioMpu) + ":" + str(real_ratioMpu))
        print(str(ratioLim) + ":" + str(real_ratioLim))

        #temp = svm.ClassifySVM(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        #pred = temp.svmTrain(self.SA_features)

        numWC = real_ratioWC * 100
        numEC = real_ratioEC * 100
        numNC = real_ratioNC * 100
        numFS = real_ratioFS * 100
        numKZN = real_ratioKZN * 100
        numNW = real_ratioNW * 100
        numGau = real_ratioGau * 100
        numMpu = real_ratioMpu * 100
        numLim = real_ratioLim * 100

        lstRatios = [numWC,numEC,numNC,numFS,numKZN,numNW,numGau,numMpu,numLim]
        print(sum(lstRatios))
        # calculate how many of the 100 people would have mental illness
        #calculate num of of the 100 that would have
        # to do this first calculate illness risk for each province
        provs = list()
        totalIll = list()
        provsHealthy = list()
        totalHealthy = list()
        for provIdx in range(0,len(expectedWeight)):
            provs.append((expectedWeight[provIdx][0]/(expectedWeight[provIdx][0]+expectedWeight[provIdx][1]))*lstRatios[provIdx]) #this is how many people out of the province percentage would be ill
            totalIll.append(provs[provIdx]*len(self.SA_features)/100)
            provsHealthy.append((expectedWeight[provIdx][1]/(expectedWeight[provIdx][0]+expectedWeight[provIdx][1]))*lstRatios[provIdx]) #how many would be healthy per province if 100 people
            totalHealthy.append(provsHealthy[provIdx]*len(self.SA_features)/100)

        
        print(expectedWeight)
        print(lstRatios)
        print(provs)
        #print(totalIll) 
        print(provsHealthy)
        print(totalHealthy)

        print(sum(totalIll)/(sum(totalHealthy)+sum(totalIll)))


    
    def display_heatmap(self):
        self.read_csv()
        self.split_data()
        self.read_csv_census()
        self.split_provinces(self.SA_features)

        t_wc = self.calcCounts(self.wc)
        t_ec = self.calcCounts(self.ec)
        t_nc = self.calcCounts(self.nc)
        t_fs = self.calcCounts(self.fs)
        t_kzn = self.calcCounts(self.kzn)
        t_nw = self.calcCounts(self.nw)
        t_gau = self.calcCounts(self.gau)
        t_mp = self.calcCounts(self.mpu)
        t_lim = self.calcCounts(self.lim)

        info = []
        info.append(t_wc)
        info.append(t_ec)
        info.append(t_nc)
        info.append(t_fs)
        info.append(t_kzn)
        info.append(t_nw)
        info.append(t_gau)
        info.append(t_mp)
        info.append(t_lim)
        return info
        

    def calcCounts(self, array):
        countWC = []
        countDisable =0
        countEmploy = 0
        countGender = 0
        countPhone=0
        countHos=0
        for person in array:
            if person[1] == '1':
                countDisable += 1
            if person[2] == '0':
                countEmploy += 1
            if person[4] == '1':
                countGender += 1
            if person[len(person) - 2] == '1':
                countPhone += 1
            if person[len(person)-1] == '1':
                countHos += 1
        countWC.append(countDisable)
        countWC.append(countEmploy)
        countWC.append(countGender)
        countWC.append(countPhone)
        countWC.append(countHos)
        return countWC

    def split_provinces(self, pred):
        for i in range (0,6553):
            self.wc.append(pred[i])
        for i in range(6553,15511):
            self.ec.append(pred[i])
        for i in range(15511,18737):
            self.nc.append(pred[i])
        for i in range(18737,22549):
            self.fs.append(pred[i])
        for i in range(22549,34800):
            self.kzn.append(pred[i])
        for i in range(34800,38975):
            self.nw.append(pred[i])
        for i in range(38975,53090):
            self.gau.append(pred[i])
        for i in range(53090,58736):
            self.mpu.append(pred[i])
        for i in range(58736,len(pred)):
            self.lim.append(pred[i])

    def country_percentage_rf(self):
        temp = rf.classifyRF(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        pred = temp.trainRF(self.SA_features)
        print(self.one_province(pred))
        return self.one_province(pred)

    def provinces_percentage_svm(self):
        percent = []
        temp = svm.ClassifySVM(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        pred = temp.svmTrain(self.SA_features)
        
        for i in range (0,6553):
            self.wc.append(pred[i])
        for i in range(6553,15511):
            self.ec.append(pred[i])
        for i in range(15511,18737):
            self.nc.append(pred[i])
        for i in range(18737,22549):
            self.fs.append(pred[i])
        for i in range(22549,34800):
            self.kzn.append(pred[i])
        for i in range(34800,38975):
            self.nw.append(pred[i])
        for i in range(38975,53090):
            self.gau.append(pred[i])
        for i in range(53090,58736):
            self.mpu.append(pred[i])
        for i in range(58736,len(pred)):
            self.lim.append(pred[i])

        percent.append(self.one_province(self.wc))
        percent.append(self.one_province(self.ec))
        percent.append(self.one_province(self.nc))
        percent.append(self.one_province(self.fs))
        percent.append(self.one_province(self.kzn))
        percent.append(self.one_province(self.nw))
        percent.append(self.one_province(self.gau))
        percent.append(self.one_province(self.mpu))
        percent.append(self.one_province(self.lim))

        return percent

    def provinces_percentage_rf(self):
        percent = []
        temp = rf.classifyRF(self.features, self.labels,self.X_test,self.X_train,self.y_test,self.y_train)
        pred = temp.trainRF(self.SA_features)
        
        for i in range (0,6553):
            self.wc.append(pred[i])
        for i in range(6553,15511):
            self.ec.append(pred[i])
        for i in range(15511,18737):
            self.nc.append(pred[i])
        for i in range(18737,22549):
            self.fs.append(pred[i])
        for i in range(22549,34800):
            self.kzn.append(pred[i])
        for i in range(34800,38975):
            self.nw.append(pred[i])
        for i in range(38975,53090):
            self.gau.append(pred[i])
        for i in range(53090,58736):
            self.mpu.append(pred[i])
        for i in range(58736,len(pred)):
            self.lim.append(pred[i])

        percent.append(self.one_province(self.wc))
        percent.append(self.one_province(self.ec))
        percent.append(self.one_province(self.nc))
        percent.append(self.one_province(self.fs))
        percent.append(self.one_province(self.kzn))
        percent.append(self.one_province(self.nw))
        percent.append(self.one_province(self.gau))
        percent.append(self.one_province(self.mpu))
        percent.append(self.one_province(self.lim))

        print(percent)

    def one_province(self, predictions):
        countH = 0
        countM = 0
        for p in predictions:
            if p == '1':
                countM += 1
            else:
                countH += 1
        total = countM + countH
        return (countM, countH)

    def write_csv(self, toWrite):
        with open(self.filename2, mode='w') as writeDS:
            ds_writer = csv.writer(writeDS, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            ds_writer.writerows(toWrite)

    def read_csv_census(self):
        
        with open(self.filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                #print(row)
                length = len(row)
                row = np.asarray(row)
                self.SA_features.append(row[1:length])
                ''' prov = row[0]
                if prov == '1':
                    wc = np.append(wc,row)
                elif prov == '2':
                    ec = np.append(ec,row)
                    #ec.append(row)
                elif prov == '3':
                    nc = np.append(nc,row)
                    #nc.append(row)
                elif prov == '4':
                    fs = np.append(fs,row)
                    #fs.append(row)
                elif prov == '5':
                    kzn = np.append(kzn,row)
                    #kzn.append(row)
                elif prov == '6':
                    nw = np.append(nw,row)
                    #nw.append(row)
                elif prov == '7':
                    gau = np.append(gau,row)
                    #gau.append(row)
                elif prov == '8':
                    mpu = np.append(mpu,row)
                    #mpu.append(row)
                elif prov == '9':
                    lim = np.append(lim,row)
                    #lim.append(row)
                else:
                    print("Error:")
                    print(row)'''

        '''for person in SA_features:
            person = np.asarray(person)
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
        wc = np.asarray(wc)
        print(wc.shape)
        ec = np.asarray(ec)
        print(ec.shape)'''
        '''self.all_prov.append(wc)
        self.all_prov.append(ec)
        self.all_prov.append(nc)
        self.all_prov.append(fs)
        self.all_prov.append(kzn)
        self.all_prov.append(nw)
        self.all_prov.append(gau)
        self.all_prov.append(mpu)
        self.all_prov.append(lim)
        self.all_prov = np.asarray(self.all_prov)
        print(self.all_prov.shape)'''
        

            

    

#path = str(".\DataSets\Mental_Illness_Survey_Matched_Converted.csv")
#mainRun = Classify()
#mainRun.country_percentage_weighted()
#mainRun.classifySVM()
#mainRun.getAll_prov_RF()
#mainRun.classifyRF()



   

    