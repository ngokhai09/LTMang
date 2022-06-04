# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:51:56 2022

@author: khai
"""

import requests
import json

if __name__=="__main__":
    r = requests.get("http://httpbin.org/get",  timeout=5)
    print("status: ", r.status_code)
    print(r.headers)
    if(r.status_code == 200):
        result = r.json()
        for i in result.items():
            print(i)
        print("Header: ")
        for header, value in r.headers.items():
            print(header, "-->", value)
        print("Header Request:")
        for header, value in r.request.headers.items():
            print(header, "-->", value)
        print("Server: ", r.headers['server'])
    else:
        print("error code %s"%r.status_code)