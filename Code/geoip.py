# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:36:19 2022

@author: khai
"""

# lay thong tin website
import requests
def geoip(domain):
    headers = {'Content-Type':'Application'}
    r = requests.get('http://freegeoip.app/json/' + domain, headers=headers)
    return r.text
if __name__=="__main__":
    print(geoip('python.org'))