# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:18:54 2022

@author: khai
"""
import urllib.request
from bs4 import BeautifulSoup
import requests

if __name__=="__main__":
    # url = "https://pixabay.com/en/photos/"    
    # data = urllib.request.urlopen(url)
    # header = {'q':'river','order':'popular','min_width':'800', 'min_height':'600'}
    
    # header = requests.utils.default_headers()
    # data = requests.get(url, params=header)
    # bs = BeautifulSoup(data.content, 'html.parser')
    # print(data.url)
    # print(bs)
    
    url = 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
    header = requests.utils.default_headers()
    data = requests.get(url, header)
    bs = BeautifulSoup(data.content, 'html.parser')
    ngay = bs.find(id="seven-day-forecast")
    dubao = ngay.find_all(class_='tombstone-container')
    # tonigt = dubao[0]
    # img = tonigt.find('img')
    # mota = img['title']
    # print(mota)
    
    list = [1,2,3,4,5,6,7]
    for i in list:
        tonight = dubao[i]
        img = tonight.find('img')
        mota = img['title']
        print(mota)