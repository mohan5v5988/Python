__author__ = 'MohanKumarVelaga'

import urllib.request
from urllib.error import  URLError
import re
import pickle


def visit_url(url, domain):
    global crawler_backlog
    global data
    st = ""
    print(st)
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        #print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            #regexp_href = re.compile('<a href=".*" title=".*">(?P<data>(.*))</a>')
            regexp_href = re.compile('<a .*>(?P<data>(.*))</a>')
            regexp_div = re.compile('<div .*>(?P<div>(.*))</div>')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            result = regexp_title.search(content_string, re.IGNORECASE)
            if result:
                title = result.group("title")
                st += str(" ")
                st += str(title)
            result = regexp_keywords.search(content_string, re.IGNORECASE)
            if result:
                keywords = result.group("keywords")
                st += str(" ")
                st += str(keywords)
            result = regexp_href.findall(content_string, re.IGNORECASE)
            if result :
                for d in result :
                    st += str(" ")
                    st += str(d[0])
            result = regexp_div.findall(content_string, re.IGNORECASE)
            if result :
                for d in result :
                    st += str(" ")
                    st += str(d[0])
            data.append((url , st))
            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
    except URLError as e:
        print("error")

crawler_backlog = {}
data = []
seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")

f = open("raw_data.pickle","br")
olddata = pickle.load(f)
f.close()
newdata = olddata + data
fi = open("raw_data.pickle","bw")
pickle.dump(newdata,fi)
fi.close()
