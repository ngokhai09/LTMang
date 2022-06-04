# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:33:14 2022

@author: khai
"""

import requests
import urllib.request
import re

if __name__=="__main__":
    user_agent = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    url = "https://mmgroup.vn/tao-email-ten-mien-voi-google/"
    # opener = urllib.request.build_opener()
    # opener.addheaders =[('User-agent', user_agent)]
    # urllib.request.install_opener(opener)
    # r = urllib.request.urlopen(url)
    # data = r.read()
    # email = re.compile("-a-zA-Z0-9._]+[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
    # email_extracted = re.findall(email, str(data))
    # print(email_extracted)
    
    data = requests.get(url).text
    print("img")
    for i in re.findall("img (.*)", data):
        for j in i.split():
            if re.findall("scr=(.*)", j):
                i = j[:-1].replace("scr=\"","")
            if(i.startswith("http")):
                print(i)
            else: 
                print(url + i)
    print("Link: ")
    for link, name in re.findall("<a(.*)>(.*)</a>", data):
        for a in link.split():
            if(re.findall("href=(.*)", a)):
                url_img = a[0:-1].replace("href\"", "")
            if(url_img.startswith("http")):
                print(url_img)
            else:
                print(url + url_img)