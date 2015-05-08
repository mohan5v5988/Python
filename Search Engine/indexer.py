__author__ = 'MohanKumarVelaga'

import os
import pickle

def indexer() :
    if os.path.isfile("raw_data.pickle") :
        f = open("raw_data.pickle","br")
        data_list = pickle.load(f)
    else :
        return "There is no file called raw_data.pickle"
    dictionary_data = {}
    for d in data_list :
        words = d[1].split()
        for word in words :
            if word in dictionary_data :
                li = dictionary_data[word]
                li.add(d[0])
                dictionary_data[word] = li
            else :
                dictionary_data[word] = {d[0]}
    return dictionary_data
#print(indexer())