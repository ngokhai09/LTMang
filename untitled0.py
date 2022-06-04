# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:07:41 2022

@author: khai
"""

import netifaces
import socket

if __name__=='__main__':
    hostname = socket.gethostname()
    print("Ten may: " + hostname)
    ipaddr = socket.gethostbyname(hostname)
    print("Dia chi ip: " + ipaddr)
    
    print("Su dung netifaces: ")
    for i in  netifaces.interfaces():
        try:
            print("IP address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print("Subnet mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
        except: pass