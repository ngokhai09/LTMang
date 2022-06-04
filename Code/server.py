# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:19:29 2022

@author: khai
"""
from time import ctime
import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.bind((host, port))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("waiting for client")
    client,  addr = sk.accept()
    print("Client address ", addr)
    client.send("hi".encode('utf-8'))
    print("Data from client: %s"%client.recv(1024).decode('utf-8'))
    while(True):
        data = client.recv(1024)    
        if not data:
            break
        so = data.decode('utf-8')
        s = so.split(' ')
        res = 0
        if(s[0] == 'p'):
            res = float(s[1]) + float(s[2])
        else :
            if(s[0] == 's'):
                res = float(s[1]) - float(s[2])       
            else:
                client.send("error".encode('utf-8'))
                break        
        data = str(res)
        client.send(data.encode('utf-8'))
        client.send("Continue?".encode('utf-8'))
        data = client.recv(1024)
        if data.decode('utf-8') == "no":
            break
        else:
            client.send("Input next: ".encode('utf-8'))
    client.close()
    sk.close()