# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:36:48 2022

@author: khai
"""

import socket
import sys

if __name__=="__main__":
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("error")
        print("%s"%str(e))
        sys.exit()
    print("Da tao socket")
    sk.connect(("www.linux.org", 80))
    while(True):
        
        data = 'GET /HTTP/1.0\r\n'
        
        sk.send(data.encode("utf-8"))
        
        data = sk.recv(1024)
        
        if not data:
            break
        print(data.decode('utf-8'))
    sk.close()
        

