#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



import numpy as np
import matplotlib.pyplot as plt
#########################################################
### your code goes here ###

from sklearn.svm import SVR
from sklearn import svm #Trying this as an alternative
from sklearn.metrics import accuracy_score
from time import time


#Add code to cut the training sets down to a more mnanagable size
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


print "\n\nBeginning to Train Model"
t0 = time()
svrLin = svm.SVC(kernel ='linear', C=1.0)  #Switched to using SVC from SVR
    #This cut processing time down by roughly 1000%
svrModel = svrLin.fit(features_train,labels_train) #Fit/Train Model
t1 = time()
print "Training model took: ", t1-t0, " Seconds"

predictions = svrModel.predict(features_test) #Predict system
score = accuracy_score(labels_test,predictions) #Get Accuracy

print "Accuracy is: ", score

#Added Feature to show stuff, not required
#plt.plot(features_test,labels_test, color='c', label = 'Linear Fit')
#plt.xlabel('data')
#plt.ylabel('target')
#plt.title('Regressions')
#plt.legend()
#plt.show()
print "Program End"
#########################################################
