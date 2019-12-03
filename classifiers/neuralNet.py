from keras.models import Sequential
from keras.utils import np_utils
from keras.layers.core import Dense, Activation, Dropout
from sklearn.model_selection import train_test_split

import tensorflow as tf
import pandas as pd
import numpy as np

class neuralNet:
    dataPath = "..\\DataSets\\Mental_Binary_Labels.csv"
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
        tf.keras.utils.normalize(dataMental, axis=-1, order=2)
        data = pd.DataFrame(dataMental)

        features = list()
        labels = list()
        
        features = data.iloc[:,1:].values
        labels = data.iloc[:,0:1].values
        
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(features, labels, test_size = 0.25)

    def classify(self):
        # Here's a Deep Dumb MLP (DDMLP)
        model = Sequential()
        model.add(Dense(128, input_dim=input_dim))
        model.add(Activation('relu'))
        model.add(Dropout(0.15))
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dropout(0.15))
        model.add(Dense(nb_classes))
        model.add(Activation('softmax'))

        # we'll use categorical xent for the loss, and RMSprop as the optimizer
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        print("Training...")
        model.fit(self.x_train, self.y_train, nb_epoch=10, batch_size=16, validation_split=0.1, show_accuracy=True, verbose=2)

        print("Generating test predictions...")
        preds = model.predict_classes(x_test, verbose=0)


        self.write_preds(preds, "keras-mlp.csv")

    def write_preds(self, preds, fname):
        pd.DataFrame({"ImageId": list(range(1,len(preds)+1)), "Label": preds}).to_csv(fname, index=False, header=True)
 
if __name__=="__main__":
    nn = neuralNet()
    nn.readInData()
    nn.classify()

