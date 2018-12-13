#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
feature_list= ["salary", "bonus"]
data = featureFormat(data_dict, feature_list)
target , features = targetFeatureSplit(data)
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.1, random_state=42)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

"""
from sklearn.linear_model import LinearRegression

reg = LinearRegression().fit(features,target)
pred = reg.predict(features)
return_data = []
for i in range(len(features)): return_data.append( [features[i], target[i], pred[i]] )
return_data.sort(key=lambda obj: (obj[2]-obj[1])**2)
print return_data[-1]
""" 


