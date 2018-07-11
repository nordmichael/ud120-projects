#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
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




#########################################################
### your code goes here ###
# Goal is to create and train a NB model to make predictions for a test set...
# Can't really remember how to do this, so that's awesome retention there buddy
# http://scikit-learn.org/stable/modules/naive_bayes.html
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from time import time
#Fit datasets
t0 = time()
myClassifySet = GaussianNB()
myClassifySet.fit(features_train,labels_train)
t1 = time()
print "\n\nTraining Time:",round(t1-t0,3),"S"

t2 = time()
predictions = myClassifySet.predict(features_test)
score = accuracy_score(labels_test,predictions)
t3 = time()
print "Predicting Time:",round(t3-t2,3),"S"
print "Accuracy Score: ", score
#Predict Data

#########################################################
