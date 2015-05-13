__author__ = 'MohanKumarVelaga'


import os
import fnmatch
import pickle

start_dir = "fortune1"
data = []

def data_load() :
    for dirpath, dirs, files in os.walk(start_dir) :
        for single_file in files :
            if fnmatch.fnmatch(single_file, "*txt") :
                f = open(os.path.join(dirpath,single_file))
                a = (os.path.join(dirpath,single_file),f.read())
                data.append(a)
                f.close()
            elif fnmatch.fnmatch(single_file, "*log") :
                f = open(os.path.join(dirpath,single_file))
                a = (os.path.join(dirpath,single_file),f.read())
                data.append(a)
                f.close()
    fi = open("raw_data.pickle","ba")
    pickle.dump(data, fi)
    print(data)
    fi.close()
#data_load()