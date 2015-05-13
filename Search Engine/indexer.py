__author__ = 'MohanKumarVelaga'

import os
import pickle
import re

spliters = " |,|-|;|:|'|\n|\t|&"
spliters1 = "[ .\n,-;\t:&?]"

def indexer() :
    if os.path.isfile("raw_data.pickle") :
        f = open("raw_data.pickle","br")
        data_list = pickle.load(f)
    else :
        return "There is no file called raw_data.pickle"
    #print(data_list)
    dictionary_data = {}
    for d in data_list :
        #print(re.split(spliters1,d[1]))
        words = re.split(spliters1,d[1]) #d[1].split()
        for word in words :
            if word in dictionary_data :
                li = dictionary_data[word]
                li.add(d[0])
                dictionary_data[word] = li
            else :
                dictionary_data[word] = {d[0]}
    return dictionary_data
#print(indexer())