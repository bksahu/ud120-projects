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
from sklearn.tree import DecisionTreeClassifier

# Define classifier
clf = DecisionTreeClassifier(min_samples_split=40)

# Initialize Time
t0 = time()
# fit the model
clf.fit(features_train, labels_train)
# Print total traininf time
print "training time for prediction:", round(time()-t0, 3), "s"

# Predict for testing set
pred = clf.predict(features_test)

# Print confidence score
print(clf.score(features_test, labels_test))
#########################################################


