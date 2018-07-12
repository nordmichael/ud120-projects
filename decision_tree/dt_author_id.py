#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
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
from sklearn import tree
from sklearn.metrics import accuracy_score
print "\n\nCreated Decision Tree Classifier"

print "Number of Training Features: ", len(features_train[0])
"""
cls_40 = tree.DecisionTreeClassifier(min_samples_split=40)

print "Beginning training data"
cls_40.fit(features_train,labels_train)

print "Fitting new Data"
cls_40_labels = cls_40.predict(features_test)

print "Calculating Accuracy"
cls_40_accuracy = accuracy_score(labels_test,cls_40_labels)

print "Decision Tree Class Accuracy: ", cls_40_accuracy
"""

#########################################################
