import urllib.request
import json


code = input("Please enter the code of the country : ")
page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/" + str(code))

if ( page.getcode() == 200 ) :
    content=page.read()
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    print("Country : " + str(json_data["name"]))
    print("capital : " + str(json_data["capital"]))
else :
    content=page.read()
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    print("Message : " + str(json_data["message"]))