from tdnn import TDNN

# Assuming 24 dim MFCCs per frame
class neuralNet_TDNN:
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
        data = pd.DataFrame(dataMental)

        features = list()
        labels = list()
        
        features = data.iloc[:,1:].values
        features = tf.keras.utils.normalize(features, axis=-1, order=2)
        labels = data.iloc[:,0:1].values
        tempLabels = list()
        # change labels to 0 and 1 to allow binary classification with keras
        for label in labels:
            if label == 1:
                tempLabels.append(0)
            else:
                tempLabels.append(1)

        labels = tempLabels
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(features, labels, test_size = 0.25)

    def classify(self):
        frame1 = TDNN(input_dim=self.x_train.shape[1], output_dim=512, context_size=5, dilation=1)
        frame2 = TDNN(input_dim=512, output_dim=512, context_size=3, dilation=2)
        frame3 = TDNN(input_dim=512, output_dim=512, context_size=3, dilation=3)
        frame4 = TDNN(input_dim=512, output_dim=512, context_size=1, dilation=1)
        frame5 = TDNN(input_dim=512, output_dim=2, context_size=1, dilation=1)