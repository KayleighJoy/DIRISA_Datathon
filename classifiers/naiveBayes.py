import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB, GaussianNB, MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import random
from statistics import mean, median

class nbClassifier:
    dataPath = "..\\DataSets\\Mental_Binary_Labels_More.csv"
    x_train = None
    x_test = None
    y_train = None
    y_test = None

    def readInData(self):
        print("reading in data")
        data = pd.read_csv(self.dataPath, sep=",") 
        print(data)
        dataMental = list()
        data = data.values
        print(data[0][0])
        countM = 0
        countH = 0
        for row in data:
            if row[0] == 2:
                #if random.randint(1,1) == 1:
                dataMental.append(row)
                countH += 1
            else:
                dataMental.append(row)
                countM += 1
        print("ratio - "+str(countH) + ":"+str(countM))
        
        data = pd.DataFrame(dataMental)
        features = list()
        labels = list()
        features = data.iloc[:,1:].values
        labels = data.iloc[:,0:1].values
        
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(features, labels, test_size = 0.25)
 
    def classifyGaussian(self):
        print("starting Gaussian")
        gnb = GaussianNB()
        gnb.fit(self.x_train, self.y_train)
        y_predict = gnb.predict(self.x_test)
        y_prob = gnb.predict_proba(self.x_test)
        countRight = 0
        countRightProb = 0
        ypredProb = list()
        for probs in y_prob:
            if probs[1]-probs[0] > 0.07:
                ypredProb.append(2)
            else:
                ypredProb.append(1)

        
        lstDiffs = list()
        for i in range(0, len(y_predict)):
            if(self.y_test[i] == 1):
                lstDiffs.append(y_prob[i][1]-y_prob[i][0])
            if (y_predict[i] == self.y_test[i]):
                countRight += 1
            if (ypredProb[i] == self.y_test[i]):
                countRightProb +=1

        print("Gaussian accuracy: "+str(countRight/len(y_predict)))
        print("Gaussian Prob Accuracy: "+ str(countRightProb/len(y_predict)))
        cnfmtx = confusion_matrix(self.y_test,ypredProb)
        clfrp = classification_report(self.y_test,ypredProb)
        print(cnfmtx)
        print(clfrp)

    def classifyComplement(self):
        print("starting Complement")
        cnb = ComplementNB()
        cnb.fit(self.x_train, self.y_train)
        y_predict = cnb.predict(self.x_test)
        y_prob = cnb.predict_proba(self.x_test)
        countRight = 0
        countRightProb = 0
        ypredProb = list()
        for probs in y_prob:
            if probs[1]-probs[0] > 0.07:
                ypredProb.append(2)
            else:
                ypredProb.append(1)

        
        lstDiffs = list()
        for i in range(0, len(y_predict)):
            if(self.y_test[i] == 1):
                lstDiffs.append(y_prob[i][1]-y_prob[i][0])
            if (y_predict[i] == self.y_test[i]):
                countRight += 1
            if (ypredProb[i] == self.y_test[i]):
                countRightProb +=1

        print("Complement accuracy: "+str(countRight/len(y_predict)))
        print("Complement Prob Accuracy: "+ str(countRightProb/len(y_predict)))
        cnfmtx = confusion_matrix(self.y_test,ypredProb)
        clfrp = classification_report(self.y_test,ypredProb)
        print(cnfmtx)
        print(clfrp)

    def classifyMultinomial(self):
        print("starting Multinomial")
        mnb = MultinomialNB()
        mnb.fit(self.x_train, self.y_train)
        y_predict = mnb.predict(self.x_test)
        countRight = 0
        for i in range(0, len(y_predict)):
            if (y_predict[i] == self.y_test[i]):
                countRight += 1
        print("Multinomial accuracy: "+str(countRight/len(y_predict)))


if __name__ == "__main__":
    clf = nbClassifier()
    clf.readInData()
    clf.classifyGaussian()
    clf.classifyMultinomial()
    clf.classifyComplement()
