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
import numpy as np
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

nan_payments , count = 0.0, 0.0
for key in enron_data.keys():
    person = enron_data[key]
    if person['poi']:
        if  person['total_payments'] == 'NaN'  : nan_payments +=1
        count += 1

print nan_payments,count,nan_payments/count











"""
#First quesion(Data space)
print "Numbers of data:",len(enron_data)
#Second question(Features space)
print "Numbers of feature for each data:",len(enron_data[enron_data.keys()[0]])
#Third question (How many POI in the data set)
count = 0
for i in range(len(enron_data)):    
    if enron_data[enron_data.keys()[i]]['poi'] is True : count+=1
print count
#Fourth question(How many POI in Enron data set)
import sys
import re
sys.path.append("../final_project/")
import poi_email_addresses
adresses = poi_email_addresses.poiEmails()
names = []
for adress in adresses:
    name = ""
    name_parts =re.findall(r"[\w']+", adress.split('@')[0])
    for name_part in name_parts:
        if len(name_part) > 1 : name += name_part
    if name not in names:
        names.append(name)
print len(names)
#Five question ( James  Prentice )

#Firstly i find the key with middleinitial
keys = enron_data.keys()
stock_features = []
for key in enron_data[keys[0]].keys():
    if "stock" in key:
        stock_features.append(key)

JP_name, JP_alt_name = "JAMES PRENTICE" ,"JAMES P"
for key in keys:
    if JP_name in key or JP_alt_name in key:
        #for features in stock_features:
           #print enron_data[key][features]
        break

#Sixt question ( Wesley Colwell )
WC_name, WC_alt_name,WC_alt2_name = "WESLEY COLWELL" ,"WESLEY C","COLWELL WESLEY"
for key in keys:
    if WC_name in key or WC_alt_name in key or WC_alt2_name in key:
        print enron_data[key]["from_this_person_to_poi"]
        break
#Seventh question ( Jeff K Skilling )JKS
JKS_name= "SKILLING JEFFREY K"
feature_samples = "exercised stock option".split(" ")
features = enron_data[JKS_name].keys()
for feature in features:
    state = True
    for sample in feature_samples : state = state and (sample in feature)
    if state is True:
        print enron_data[JKS_name][feature]
        break

JS , AF , KL = "SKILLING JEFFREY K" , "FASTOW ANDREW S" , "LAY KENNETH L"
NAMES = ["SKILLING JEFFREY K" , "FASTOW ANDREW S" , "LAY KENNETH L"]
max_payment , max_name = 0 , ""
for name in NAMES:
    if enron_data[name]["total_payments"] > max_payment:
        max_payment = enron_data[name]["total_payments"]
        max_name = name
print max_name,max_payment


"""

