# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:20:33 2022

@author: khai
"""

import socket
host = '127.0.0.1'
port = 9050

def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind((host, port))
    sk.listen(10)
    return sk

def recv_msg(sk):
    #nhan den khi gap null
    data = bytearray()
    msg = ''
    # doc 1024 byte den khi gap null
    while not msg:
        data_p = sk.recv(1024)
        if not data_p:
            raise ConnectionError()
        data = data + data_p
        if b'\0' in data_p:
            # b'\0' la ky tu cuoi cung
            msg = data.rstrip(b'\0')
    return msg.decode('utf-8')

def create_msg(msg):
    #them null vao mess
    msg += '\0'
    return msg.encode('utf-8')

def send_msg(sk, msg):
    data = create_msg(msg)
    sk.sendall(data)