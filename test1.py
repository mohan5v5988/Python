import os
import fnmatch
import pickle

start_dir = "fortune1"
data = []

def traverser_data() :
    for dirpath, dirs, files in os.walk(start_dir) :
        for single_file in files :
            if fnmatch.fnmatch(single_file, "*txt") :
                f = open(os.path.join(dirpath,single_file))
                a = (os.path.join(dirpath,single_file),f.read())
                data.append(a)
                f.close()
    fi = open("raw_data.txt","bw")
    pickle.dump(data, fi)
    print(data)
    fi.close()
traverser_data()