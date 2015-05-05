import os

def search(data , word) :
    lo = set()
    words = data.split()
    for i , w in enumerate(words) :
        if ( w == word ) :
            lo.add(i)
    return lo

fileName = input(" File Name : ")
f = open( os.path.join( os.getcwd() , fileName ), "r")
data_list = f.read()
h = search(data_list , "password=")
if ( not h ) :
    print("It is not there")
else :
    print("found at these locations = " + str(h))