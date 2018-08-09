#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# Remove total
data_dict.pop('TOTAL')
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
# Plot data
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# Max Salary
#max_salary = max([point[1] for point in data])
#max_guy = [key for key in data_dict.keys() if data_dict[key]['salary'] == max_salary]

# List of outliers
top_salarys = sorted([point[0] for point in data if point[1] > 1000000], reverse=True)
top_two = [key for key in data_dict.keys() if data_dict[key]['salary'] == top_salarys[0] or data_dict[key]['salary'] == top_salarys[1]]