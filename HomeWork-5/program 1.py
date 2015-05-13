__author__ = 'MohanKumarVelaga'

import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
    global crawler_backlog
    if(len(crawler_backlog)>10):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
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
                print(title)
            result = regexp_keywords.search(content_string, re.IGNORECASE)
            if result:
                keywords = result.group("keywords")
                print(keywords)
            #result = regexp_href.search(content_string, re.IGNORECASE)
            result = regexp_href.findall(content_string, re.IGNORECASE)
            print(result)
            if result :
                for d in result :
                    print(d[0])
            result = regexp_div.findall(content_string, re.IGNORECASE)
            print(result)
            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")
