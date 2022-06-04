# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:23:42 2022

@author: khai
"""

from urllib.request import urlopen
import urllib.error
from urllib.request import Request
import gzip

if __name__ == "__main__":
    try:
        header = {'Accept-Language':'vn'}
        #Tao doi tuong request
        req = Request("http://www.vnexpress.net")
        #them header
        req.add_header('Accept-Encoding', 'gzip')
        #gui request them option bang urlopen
        respone = urlopen(req)
        #respone = urlopen("http://www.python.org")
        # print(respone)
        # print("url: ", respone.url)
        # print("status: ", respone.code)
        # print(respone.readline())
        # print(respone.read())
        # print(respone.getheaders())        
        # print(req.header_items())
        # print(respone.getheader('Content-Encoding'))
        data = gzip.decompress(respone.read())
        print(data)
        print(respone.getheader('Content-Type'))
    except urllib.error.HTTPError as err:
        print("status: ", err.status)