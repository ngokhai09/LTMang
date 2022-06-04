# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:20:99 2022

@author: khai
"""

import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.connect((host,port))
    sk.send("hi".encode('utf-8'))
    data = sk.recv(1024)
    print("Data from server: %s"%data.decode('utf-8'))
    while True:
        data = input("nhap: ")
        sk.send(data.encode('utf-8'))
        data = sk.recv(1024)
        print("Data from server: %s\n"%data.decode('utf-8'))
        data = sk.recv(1024)
        if data.decode('utf-8') == "error":
            print("Syntax Error")
            break
        print("Data from server: %s\n"%data.decode('utf-8'))
        data = input("Yes/No?")
        sk.send(data.encode('utf-8'))
        if data == "no":
            break
        
    sk.close()