__author__ = 'MohanKumarVelaga'

import indexer

def search(dictionary_data,out,op) :
    if (op == "and") :
        output = dictionary_data[out[0]]
        for i in range(1, len(out)) :
            output = output & dictionary_data[out[i]]
    else :
        output = dictionary_data[out[0]]
        for i in range(1, len(out)) :
            output = output | dictionary_data[out[i]]
    output = sorted(output)
    print("The word is found in these files : " + str(output))