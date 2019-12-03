#Class for random forest
import pandas as pd  
import numpy as np  
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
import time 
import datetime
import os
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from itertools import cycle
import seaborn as sns

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, roc_auc_score, auc
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import label_binarize, OneHotEncoder, LabelEncoder
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.ensemble import RandomForestClassifier

class classifyRF:
    def __init__(self, features, labels, X_test, X_train, y_test, y_train):
        self.features = features
        self.labels = labels
        self.X_test = X_test
        self.X_train = X_train
        self.y_test = y_test
        self.y_train = y_train
        self.confusion = None
        self.report = None
        self.misclassifiedIndex = None

    def findBestParameters(self, rf):
        param_grid = {'n_estimators': [1000, 750, 500, 200, 100],
                    'max_features': ['auto', 'sqrt'],
                    'max_depth' : [int(x) for x in np.linspace(10, 110, num = 11)],
                    'criterion' :['gini', 'entropy'],
                    }

        cross_validation = StratifiedKFold(n_splits=10)

        grid_search = GridSearchCV(rf,
                                param_grid=param_grid,
                                cv=10)
        grid_search.fit(self.X_train, self.y_train)
        best = grid_search.best_estimator_
        bestParams = grid_search.best_params_
        print(best)
        print(bestParams)
        return best

    def trainRF(self, toPredict):
        print("Training for prediction")
        model = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                       max_depth=85, max_features='auto', max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=200,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(toPredict)
        return y_pred

    def trainRfForMetrics(self, name):
        print("Train for metrics")
        #X_train, X_test, y_train, y_test = train_test_split(self.featuredData, self.proper_labels, test_size = 0.20)
        #model = RandomForestClassifier(n_estimators=500, criterion="entropy")
        model = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
                       max_depth=110, max_features='auto', max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=200,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
        #model = self.findBestParameters(model)
        model.fit(self.X_train, self.y_train)

        y_pred = model.predict_proba(self.X_test)
        y_pred2 = model.predict(self.X_test)

        self.misclassifiedIndex = []
        for x in range(len(y_pred2)):
            if y_pred2[x] != self.y_test[x]:
                self.misclassifiedIndex.append(x)

        self.confusion = confusion_matrix(self.y_test,y_pred2)
        self.report = classification_report(self.y_test,y_pred2)

        metrics = [self.confusion, self.report]

        with open("RandomForestLog.txt", mode='a') as writeDS:
            ds_writer = csv.writer(writeDS, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            ds_writer.writerows(metrics)

        onehot_encoder = OneHotEncoder(sparse=False)
        y_tests = onehot_encoder.fit_transform(self.y_test)

        print(y_pred)

        n_classes = y_tests.shape[1]
        print(y_tests)
        lw = 2

        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_tests[:, i], y_pred[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])

        # Compute micro-average ROC curve and ROC area
        fpr["micro"], tpr["micro"], _ = roc_curve(y_tests.ravel(), y_pred.ravel())
        roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

        #plot curve
        all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

        # Then interpolate all ROC curves at this points
        mean_tpr = np.zeros_like(all_fpr)
        for i in range(n_classes):
            mean_tpr += interp(all_fpr, fpr[i], tpr[i])

        # Finally average it and compute AUC
        mean_tpr /= n_classes

        fpr["macro"] = all_fpr
        tpr["macro"] = mean_tpr
        roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

        # Plot all ROC curves
        fig, (ax1, ax2) = plt.subplots(nrows=1,ncols=2,figsize=(10,5))
        ax1= plt.subplot(1,2,1)
        index = ['Mental','Healthy']  
        columns = ['Mental','Healthy']  
        cm_df = pd.DataFrame(self.confusion,columns,index)
        sns.heatmap(cm_df, annot=True, ax = ax1, fmt='g')

        ax2 = plt.subplot(1, 2,2)
        ax2.plot(fpr["micro"], tpr["micro"],
                label='micro-average ROC curve (area = {0:0.2f})'
                    ''.format(roc_auc["micro"]),
                color='deeppink', linestyle=':', linewidth=4)

        ax2.plot(fpr["macro"], tpr["macro"],
                label='macro-average ROC curve (area = {0:0.2f})'
                    ''.format(roc_auc["macro"]),
                color='navy', linestyle=':', linewidth=4)

        colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
        for i, color in zip(range(n_classes), colors):
            ax2.plot(fpr[i], tpr[i], color=color, lw=lw,
                    label='ROC curve of class {0} (area = {1:0.2f})'
                    ''.format(i, roc_auc[i]))

        ax2.plot([0, 1], [0, 1], 'k--', lw=lw)
        ax2.set_xlim([0.0, 1.0])
        ax2.set_ylim([0.0, 1.05])
        ax2.set_xlabel('False Positive Rate')
        ax2.set_ylabel('True Positive Rate')
        fig.suptitle('ROC - RF More Data')
        ax2.legend(loc="lower right")
        plt.savefig(name)
        
        return plt.plot
    
    def getConfusion(self):
        return self.confusion

    def getReport(self):
        return self.report

    def getIndexes(self):
        misFeaturesIndex = []
        for x in self.misclassifiedIndex:
            misFeaturesIndex.append(self.features.index(self.X_test[x]))
        return misFeaturesIndex