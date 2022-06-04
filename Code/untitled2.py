# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:21:47 2022

@author: khai
"""

from urllib.request import urlopen 
from urllib.request import Request
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import datetime

if __name__ == "__main__":
    r = Request("http://www.gmail.com")
    r1 = urlopen(r)
    # print(r1.url)
    print(r.redirect_dict)
    
    # r = Request('http://www.python.org')
    # r1 = urlopen(r)
    # print(r.get_header('User-agent'))
    #Tao ko gian luu cookie
    # cj = CookieJar()
    #Tao urllib builder -> tu dong lay cookie tu response cua server
    # opener = build_opener(HTTPCookieProcessor(cj))
    # tao http request 
    # v = opener.open("http://www.github.com")
    # print(v)
    # print(len(cj))
    #Cookiejar ko cho phep truy cap truc tiep -> Tao list de lay tung cookie
    # cookies = list(cj)
    # print(cookies)
    # print("cookie 0:")
    # print(cookies[0].name)
    # print(cookies[0].value)
    # print(cookies[0].domain)
    # print(cookies[0].path)
    # print(cookies[0].expires) #unix time
    # print(datetime.datetime.fromtimestamp(cookies[0].expires))
    # print(cookies[0].secure)
   