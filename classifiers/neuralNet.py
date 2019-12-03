from keras.models import Sequential
from keras.utils import np_utils
from keras.layers.core import Dense, Activation, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

import keras
import tensorflow as tf
import pandas as pd
import numpy as np

class neuralNet:
    dataPath = "..\\DataSets\\Mental_Binary_Labels_More.csv"
    x_train = None
    x_test = None
    y_train = None
    y_test = None
    features = None
    cats = None

    def readInData(self):
        print("reading in data")
        data = pd.read_csv(self.dataPath, sep=",") 
        print(data)
        dataMental = list()
        data = data.values
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

        dataMental = np.asarray(dataMental)
        print("ratio - "+str(countH) + ":"+str(countM))
        #normalise data
        data = pd.DataFrame(dataMental)

        self.features = list()
        labels = list()
        
        self.features = data.iloc[:,1:].values
        self.cats = data.iloc[:,1:].values
        self.features = tf.keras.utils.normalize(self.features, axis=-1, order=2)
        labels = data.iloc[:,0:1].values
        tempLabels = list()
        # change labels to 0 and 1 to allow binary classification with keras
        for label in labels:
            if label == 1:
                tempLabels.append(0)
            else:
                tempLabels.append(1)

        labels = tempLabels
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.features, labels, test_size = 0.25)

    def classify(self):
        # Here's a Deep Dumb MLP (DDMLP)
        self.y_train = np_utils.to_categorical(self.y_train) 
        self.y_test = np_utils.to_categorical(self.y_test) 
        #print(self.y_train.shape)
        input_dim = self.x_train.shape[1]
        numClasses = 2
        print("Input Dimension: ",input_dim)
        model = Sequential()
        model.add(Dense(8, input_dim=input_dim))
        model.add(Dense(16))
        model.add(Dense(32))
        model.add(Activation('relu'))
        model.add(Dense(8))
        model.add(Dense(8))
        model.add(Activation('relu'))
        model.add(Dense(numClasses))
        model.add(Activation('softmax'))

        # we'll use categorical xent for the loss, and RMSprop as the optimizer
        # model.compile(loss='binary_crossentropy', optimizer='rmsprop')
        # model.compile(loss='sparse_categorical_crossentropy', optimizer=keras.optimizers.Adam(lr=0.001), metrics=['accuracy'])
        # model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
        model.compile(loss='binary_crossentropy',  optimizer=keras.optimizers.Adam(lr=0.001), metrics=['accuracy'])
        
        print("Training...")
        model.fit(self.x_train, self.y_train, epochs=100, batch_size=16, verbose=1, validation_data=(self.x_test,self.y_test))

        print("Generating test predictions...")
        preds = model.predict_classes(self.x_test, verbose=0)
        #self.y_test = np_utils.to_categorical(self.y_test) 
        #score = model.evaluate(self.x_test, self.y_test, batch_size=16)
        #print(score)
        tempLbl = list()
        for lbl in self.y_test:
            if lbl[0] == 1:
                tempLbl.append(0)
            else:
                tempLbl.append(1)
        
        self.y_test = tempLbl

        print(self.y_test)
        print(preds)

        cnfmtx = confusion_matrix(self.y_test,preds)
        clfrp = classification_report(self.y_test,preds)
        print(cnfmtx)
        print(clfrp)


        self.write_preds(preds, "keras-mlp.csv")

    def write_preds(self, preds, fname):
        pd.DataFrame({"ImageId": list(range(1,len(preds)+1)), "Label": preds}).to_csv(fname, index=False, header=True)
 
    def getCats(self):
        tempCats = []
        for feat in self.cats[0]:
            tempCats.append([])
        #create cats for each 
        for row in self.cats:
            for f in range(0,len(row)):
              tempCats[f].append(row[f])

        for features in tempCats:
            print(features)
            features = np_utils.to_categorical(features)
            print("==== showing cats ==== ")
            print(features)
            

                
         

if __name__=="__main__":

    nn = neuralNet()
    nn.readInData()
    nn.classify()
    #nn.getCats()
