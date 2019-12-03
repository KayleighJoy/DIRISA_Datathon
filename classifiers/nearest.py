from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB, GaussianNB, MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
import random
from statistics import mean, median
import pandas as pd

neigh = KNeighborsClassifier(n_neighbors=7)
dataPath = "..\\DataSets\\Mental_Binary_Labels_More.csv"

x_train = None
x_test = None
y_train = None
y_test = None

data = pd.read_csv(dataPath, sep=",")
features = data.iloc[:,1:].values
labels = data.iloc[:,0:1].values

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.10)

neigh.fit(x_train, y_train)
preds = neigh.predict(x_test)
cnfmtx = confusion_matrix(y_test,preds)
clfrp = classification_report(y_test,preds)
print(cnfmtx)
print(clfrp)