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
# import Gaussian Naive Bayes (GaussianNB)
from sklearn.naive_bayes import GaussianNB

# define the classifier
clf = GaussianNB()


# initialize the time t0
t0 = time()
# fit the model
clf.fit(features_train, labels_train)
# print the total training time
print "training time for fitting:", round(time()-t0, 3), "s"


# initialize the time t0
t0 = time()
# predict for the testing set
clf.predict(features_test)
# print the total training time
print "training time for prediction:", round(time()-t0, 3), "s"


# print the score
print clf.score(features_test, labels_test)

