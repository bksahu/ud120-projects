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

# Split into 1% of total
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(kernel='rbf', C=10000)


t0 = time()

# fit the model
clf.fit(features_train, labels_train)

# print the total training time
print "training time for fitting:", round(time()-t0, 3), "s"


# print the confidence score
print(clf.score(features_test, labels_test))

pred = clf.predict(features_test)

# print the 10th, 26th, 50th prediction
print(pred[10], pred[26], pred[50])

# count total number of occurence of both the classes
from collections import Counter
print(Counter(pred))
#########################################################


