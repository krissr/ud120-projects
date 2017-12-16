#!/usr/bin/python
# -*- coding: utf-8 -*-
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




#########################################################
### your code goes here ###
from sklearn import svm

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(C=10000.0, kernel="rbf", verbose=True)

t0 = time()
clf.fit(features_train, labels_train)
print("Training time:", round(time()-t0, 3), "s")

pred = clf.predict(features_test)

print pred

print pred[10]
print pred[26]
print pred[50]

print sum(pred)

t0 = time()
print(clf.score(features_test, labels_test))
print("Accuracy:", round(time()-t0, 3), "s")
#########################################################


