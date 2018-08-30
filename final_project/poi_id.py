#!/usr/bin/python

import sys
import cPickle as pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'salary', 'bonus', 'ratio_to_poi_email', 'ratio_to_poi_email']


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Task 2: Remove outliers
for key in ["TOTAL", "THE TRAVEL AGENCY IN THE PARK", "LOCKHART EUGENE E"]:
    my_dataset.pop(key, 0)
    
### Task 3: Create new feature(s)
### New features are ratio_to_poi_email & ratio_from_poi_email

import numpy as np
ratios = np.zeros((len(my_dataset), 2))
for i, key in enumerate(my_dataset.keys()):
    ratios[i, 0] = float(my_dataset[key]['from_this_person_to_poi'])/float(my_dataset[key]['from_messages'])
    ratios[i, 1] = float(my_dataset[key]['from_poi_to_this_person'])/float(my_dataset[key]['to_messages'])

###  Drop NaN
from sklearn.preprocessing import Imputer
ratios = Imputer().fit_transform(ratios)

### Add two new fields in my_dataset
for i, key in enumerate(my_dataset.keys()):
    my_dataset[key]['ratio_to_poi_email'] = ratios[i,0]
    my_dataset[key]['ratio_from_poi_email'] = ratios[i,1]



### Get data from the data dict
data = featureFormat(my_dataset, features_list, sort_keys = True)
### Extract features and labels from dataset for local testing
labels, features = targetFeatureSplit(data)


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler().fit(features)
features = scaler.transform(features)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html


#from sklearn.tree import DecisionTreeClassifier
#clf = DecisionTreeClassifier()

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)