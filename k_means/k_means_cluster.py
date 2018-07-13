#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

""" Added code to display max and min values from exercised_stock_options where things """
""" Modified code to take a more universal variable to pick max/min of other values"""
min_value = 100000000
max_value = 0
interested_feature = "salary"#'exercised_stock_options'
for label in data_dict:
    if (data_dict[label][interested_feature] != 'NaN') and (data_dict[label][interested_feature] > 0):
        #print label, ":", data_dict[label]['exercised_stock_options']
        if (data_dict[label][interested_feature] > max_value):
            max_value = data_dict[label][interested_feature]
        if (data_dict[label][interested_feature] < min_value):
            min_value = data_dict[label][interested_feature]
print interested_feature, "max: ", max_value
print interested_feature, "min: ", min_value


### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3] #Added total payments
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

#print "Printing finance features"
#new_ff1 = map(list, zip(*finance_features))
#print new_ff1

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2 )
#plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
"""Deploy k-means clustering on the financial_features data, with 2 clusters
    specified as a parameter. Store your cluster predictions to a list called pred,
    so that the Draw() command at the bottom of the script works properly.
    In the scatterplot that pops up, are the clusters what you expected?"""
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
pred = kmeans.fit(finance_features).predict(finance_features)


"""Add Scaling here for now"""
from sklearn.preprocessing import MinMaxScaler
all_scaler = MinMaxScaler()
rescaled_features = all_scaler.fit_transform(finance_features)
print all_scaler.transform([[200000,1000000,0]])
#print rescaled_features
#rescaled_f1 = scaler_f1.fit_transform(new_ff1[0])
#rescaled_f2 = scaler_f2.fit_transform(new_ff1[1])
#print "Scaled Salary:", scaler_f1.transform(200000)
#print "Scaled Stock Option:", scaler_f2.transform(200000)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
