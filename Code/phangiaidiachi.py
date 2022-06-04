# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:17:26 2022

@author: khai
"""

# phan giai dia chi
import socket
if __name__=="__main__":
    try:
        r = socket.gethostbyaddr('8.8.8.8')
        print("host name: ", r[0])
        for i in r[2]:
            print(""+i)
    except socket.error as e:
        print("error")