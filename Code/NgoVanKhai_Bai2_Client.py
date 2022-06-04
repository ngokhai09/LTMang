# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:42:23 2022

@author: khai
"""

import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.connect((host,port))
    data = "hello"

    data = input("Nhap Chuoi: ")
    sk.send(data.encode('utf-8'))
    data = sk.recv(1024)
    print("Chuoi da chuan hoa: %s"%data.decode('utf-8'))
    sk.close()