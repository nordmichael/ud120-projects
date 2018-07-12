#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    numPop = int(0.10*len(predictions))
    errorVals = []
    fullList = []
    for index in range(0,len(predictions)):
        errorVals = abs(max(predictions[index]) - max(net_worths[index]))
        fullList.append([max(predictions[index]),max(ages[index]),max(net_worths[index]),errorVals])

    #sort the list according to last row
    fullList.sort(key=lambda x: x[3])

    #Pop last items
    for index in range(0,numPop):
        fullList.pop()
    #print fullList
    #for item in fullList:
    #    print item

    #Prepare cleaned data for passing back
    for index in range (0,len(fullList)):
        cleaned_data.append([fullList[index][1],fullList[index][2],fullList[index][3]])

#    sortedList = sorted(fullList[1])
#    print sortedList

    return cleaned_data
