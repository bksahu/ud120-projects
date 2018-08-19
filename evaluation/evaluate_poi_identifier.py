#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import cPickle as pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels,
                                                                            random_state=42, test_size=0.3)

### it's all yours from here forward!  
from sklearn.tree import DecisionTreeClassifier

# Define classifier
clf = DecisionTreeClassifier()

# fit the model
clf.fit(features_train, labels_train)

# Predict for testing set
pred = clf.predict(features_test)

# Print confidence score
print(clf.score(features_test, labels_test))

# Total poi identified for the test set
import numpy as np
np.sum(pred ==1)

# Total people in test set
len(features_test)

## identifier predicted 0. (not POI) for everyone in the test set
#pred_0 = pred
#pred_0[pred_0 == 1] = 0
#print float(np.sum(pred_0 == labels_test))/len(labels_test)

# Get precision_score
from sklearn.metrics import precision_score
precision_score(labels_test, pred)

# Get recall_score
from sklearn.metrics import recall_score
recall_score(labels_test, pred)