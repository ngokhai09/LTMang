# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:06:31 2022

@author: khai
"""


import socket
host = '127.0.0.1'
port = 9050
if __name__=="__main__":
    try:
        print('gethostname:', socket.gethostname())
        print('gethostbyname:', socket.gethostbyname('www.google.com'))
        print('gethostbyaddr:', socket.gethostbyaddr('8.8.8.8'))
        print('getfqdn ', socket.getfqdn('www.google.com'))
        print('getaddrinfo: ', socket.getaddrinfo('www.google.com', None, 0, socket.SOCK_STREAM))
    except socket.error as e:
        print(str(e))
        print('error')