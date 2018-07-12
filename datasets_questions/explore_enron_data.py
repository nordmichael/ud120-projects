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
print "Found: ", count_poi_names, " Persons of Interest"

#Collect total stock value for James Prentis
print "\nFinding James Prentis information"
for name in enron_data:
    if name.find("PRENTICE JAMES") >= 0 :
        print "Found Person: ", name
        print enron_data[name]["total_stock_value"]

#Find quantity of email messages do we have from Wesley Colwell to persons of interest
#enron_data["LASTNAME FIRSTNAME"]["feature_name"]
print "\nFinding Wesley Colewell information"
for name in enron_data:
    if name.find("COLWELL WESLEY") >= 0 :
        print "Found Person: ", name
        print "From this person to POI: ", enron_data[name]['from_this_person_to_poi']
        #for element in enron_data[name]:
        #    print element, " : ", enron_data[name][element]


#Find stock option value exercised by Jeffrey K Skilling
print "\nFinding Jeffrey K Skilling information"
for name in enron_data:
    if name.find("SKILLING") >= 0 :
        print "Found Person: ", name
        print "Stock Option Exercised Value: ", enron_data[name]['exercised_stock_options']
        for element in enron_data[name]:
            print element, " : ", enron_data[name][element]

#Find Total payments recieved by Ken Lay
print "\nFinding Ken Lay Skilling information"
for name in enron_data:
    if name.find("LAY KEN") >= 0 :
        print "Found Person: ", name
        print "Total Payments: ", enron_data[name]['total_payments']
        for element in enron_data[name]:
            print element, " : ", enron_data[name][element]


#Find number of people with quantified Salary and known email addresses
print "\nFinding Number of people with quantified Salary"
count_salary = 0
count_email = 0
for name in enron_data:
    if enron_data[name]['salary'] != 'NaN':
        count_salary += 1
    if len(enron_data[name]['email_address']) > 5:
        count_email += 1
print "Salary Count: ", count_salary
print "Count Email: ", count_email

#Find number of people with NaN for total payments
print "\nFinding number of people with absent total payment information"
count_iter = 0
count_total_payments = 0
count_poi_total_payment_nan = 0
for name in enron_data:
    count_iter += 1
    if enron_data[name]['total_payments'] == 'NaN':
        count_total_payments += 1
        if enron_data[name]['poi'] == True:
            count_poi_total_payment_nan +=1
print "Num Total Payments NaN: ", count_total_payments
print "Total Num people: ", count_iter
print "Percentage total payments NaN: ", str((float(count_total_payments)/float(count_iter))*100.0)
print "Total Poi Nan Total Payment: ", count_poi_total_payment_nan
