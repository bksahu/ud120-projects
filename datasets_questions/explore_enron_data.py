#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Total no. of people/datapoints
print(len(enron_data))

# No of feature per person
len(enron_data["SKILLING JEFFREY K"])

# Total person of interest
TotalPoi = 0
for person in enron_data:
    if enron_data[person]['poi'] == 1:
        TotalPoi += 1
print TotalPoi        
       
# Total value of the stock belonging to James Prentice        
print enron_data["PRENTICE JAMES"]['total_stock_value']      

# total email messages from Wesley Colwell to poi
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']  

# value of stock options exercised by Jeffrey K Skilling
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


# Max total payments
smartest_guy = [(key,enron_data[key]['total_payments']) for key in enron_data.keys() if key == 'FASTOW ANDREW S' or key == 'LAY KENNETH L' or key == 'SKILLING JEFFREY K']
print smartest_guy

# Check if email exists
email_guys = [(key,enron_data[key]['email_address']) for key in enron_data.keys() if enron_data[key]['email_address'] != 'NaN']
print len(email_guys)

# Check if quantified salary
salary_guys = [(key,enron_data[key]['salary']) for key in enron_data.keys() if enron_data[key]['salary'] != 'NaN']
print len(salary_guys)

# Percentage of people having 'NaN' in their total payments
NaN_guys = len([(key) for key in enron_data.keys() if enron_data[key]['total_payments'] == 'NaN'])
print float(NaN_guys)/len(enron_data) * 100

# Percentage of people having 'NaN' in their total payments
Poi_NaN_guys = len([(key) for key in enron_data.keys() if enron_data[key]['total_payments'] == 'NaN' and  enron_data[key]['poi'] == True])
print float(Poi_NaN_guys)/len(enron_data) * 100










