__author__ = 'MohanKumarVelaga'

import indexer
import searcher
import urllib.request
import json
from urllib.error import URLError


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

try :
    page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+"06516")
    code = page.getcode()
    if(code == 200 ) :
        content=page.read()
        content_string = content.decode("utf-8")
        json_data = json.loads(content_string)
        name = json_data["name"]
        weather = json_data["weather"][0]["main"]
        sun_rise = json_data["sys"]["sunrise"]
        sun_set = json_data["sys"]["sunset"]
except URLError as e :
    print("error")



dictionary_data = indexer.indexer()
print()
print("location : " + str(name) + " Weather : " + str(weather) + " Sun Rise : " + str(sun_rise) + " Sun Set : " + str(sun_set))
print()
searcher.search(dictionary_data,out,op)

