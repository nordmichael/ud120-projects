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

#Count total number of people in dataset
print "Number of People: ", len(enron_data)

#print enron_data.viewkeys()

#Get total intersect of dataset and people of interest
poi_count = 0
for person in enron_data:
    if enron_data[person]["poi"] == True:
        poi_count += 1
print poi_count


#Get person of interest names from poi names file
#Discard first line because it's a web address
f_poi_names = open("../final_project/poi_names.txt",'r')
f_poi_names.readline()
count_poi_names = 0
for name in f_poi_names:
    if len(name) > 1:
        #print "Name: ", name
        count_poi_names += 1
print count_poi_names
