import pandas as pd
from sklearn import datasets
from sklearn.naive_bayes import ComplementNB, GaussianNB, MultinomialNB

iris = datasets.load_iris()

cnb = GaussianNB()
yped = cnb.fit(iris.data, iris.target).predict(iris.data)
numWrong = 0
for i in range(0, len(yped)):
    if not(yped[i] == iris.target[i]):
        numWrong += 1
print("Num mislabeled : "+str(numWrong))
