#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL",0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for key , values in data_dict.items():
    salary=float(values.get("salary"))
    bonus=float(values.get("bonus"))
    if(salary>1000000 and bonus>=5000000):
        print(key)

### your code below


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
maxBonus = 0
itemCap = ""
index = 0

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
