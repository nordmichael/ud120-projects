#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )

from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remo ve this line to run over full dataset
        temp_counter += 1
        if 1: # temp_counter 1 < 200: #Commented out to run code on whole list

            path = os.path.join('..', path[:-1])
            #print path #Commented out to improve speed of running
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            parsedText = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            parsedText.replace("sara","")
            parsedText.replace("shackleton","")
            parsedText.replace("chris","")
            parsedText.replace("germani","")
            #print "ParsedText:\n", parsedText
            word_data.append(parsedText)
            ### append the text to word_data
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                from_data.append(0)
            elif name == "chris":
                from_data.append(1)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

#Print out stuff as required
pr_line = 152
print "Word_data line:",pr_line,"contents is: ", word_data[152]
print "From_data line:",pr_line,"contents is: ", from_data[152]


#Prebuilt pickle function to dump list of authors and data
pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
transformer = TfidfVectorizer(stop_words="english")
word_data_trans = transformer.fit_transform(word_data)

#print transformer.get_feature_names()    #Don't really need to print an array of words anymore
print "LENGTH: ", len(transformer.get_feature_names())
word_list = transformer.get_feature_names()
print "Word Number X: ",
for index in range(0, len(word_list)):
    if ((index >= (34597-20)) and (index < (34597+200))):
        print "Index:", index, "Word: ", word_list[index]
