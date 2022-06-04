# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:21:22 2022

@author: khai
"""

# scan port
import optparse
from socket import *
import socket
from threading import *

def socketscan(host, port):
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(5)
        r = sk.connect((host,port))
        print("TCP opened ", port)
    except Exception as e:
        print("TCP closed ", port)
        print(str(e))
    finally:
        sk.close()
def portscan(host, port):
    try:
        ip = gethostbyname(host)
        print("Scan result: " + ip)
    except:
        print("Khong the phan giai dia chi")
        return
    for i in port:
        t = Thread(target=socketscan, args=(ip, int(i)))
        t.start()
        
if __name__=="__main__":
    host = 'www.google.com'
    port = 80,81,21,22,443
    portscan(host, port)