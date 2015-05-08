import os
import pickle
def user(data) :
    name = input("Please enter the name : ")
    age = input("Please enter the age : ")
    origin = input("Please enter the Origin : ")
    data[name] = (age , origin)
    return data

def readData(data) :
    if ( os.path.isfile("data.pickle") ) :
        f = open("data.pickle","br")
        data = pickle.load(f)
    return data

data = {}
data = readData(data)
data = user(data)
f = open("data.pickle","bw")
pickle.dump(data,f)
print(data)