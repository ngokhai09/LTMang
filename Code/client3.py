# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:53:53 2022

@author: khai
"""

import socket
host = '127.0.0.1'
port = 9050
if __name__=="__main__":
    print("ket noi %s tren cong la %s"%(host,port))
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host, port))
    sk.send(bytes('GET / HTTP/1.1\r\nhost: localhost\r\n\r\n'.encode('utf-8')))
    respone = sk.recv(1024)
    print("server reply %s"%host)
    print(respone.decode('utf-8'))
    
    