# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:38:53 2022

@author: khai
"""

import urllib.request

if __name__=="__main__":
    url = "https://www.python.org/static/img/python-logo.png"
    urllib.request.urlretrieve(url, "img.png")
    r = urllib.request.urlopen(url)
    print("Status: ", r.status)
    image = open("img.png", "wb")
    image.write(r.read())