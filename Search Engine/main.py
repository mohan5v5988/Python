__author__ = 'MohanKumarVelaga'

import indexer
import searcher


def nitherisgiven(li) :
    for a in li :
        if (a == "and") :
            return False
        elif (a == "or") :
            return False
    return True
# main function
array = []
name = input("query :")
temp = name.split(" ")
temp1 = set()
op = "or"
if (nitherisgiven(temp)) : op = "and"
for t in temp :
    if ( t == "and" ) :
        op = "and"
    elif ( t != "or" ) :
        temp1.add(t)
print( "Performing '" + op.upper() + "' search for: " + str(temp1) )
out = list(temp1)

dictionary_data = indexer.indexer()
searcher.search(dictionary_data,out,op)