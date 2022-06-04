# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:47:39 2022

@author: khai
"""

import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(5)
    while True:
        print("Listening...")
        client_sk, addr = sk.accept()
        print("Http receive:")
        print(client_sk.recv(1024))
        client_sk.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello world</h1></body></html> \r\n", 'utf-8'))
        client_sk.close()