def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    ### create classifier
    myCls = GaussianNB()
    ### fit the classifier on the training features and labels
    myCls.fit(features_train,labels_train)

    ### return the fit classifier
    return myCls

    ### your code goes here!

    
