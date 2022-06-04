# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:46:46 2022

@author: khai
"""

import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.connect((host,port))
    data = input("Nhap ten file: ")
    
    try:
        f = open(data, 'rb')
        sk.send(data.encode('utf-8'))
        data = f.read()
        sk.send(data) 
    except FileNotFoundError:
        print("Khong tim thay file")
    data = sk.recv(1024)
    print(data.decode('utf-8'))
    sk.close()