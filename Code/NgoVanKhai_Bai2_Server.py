# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:16:46 2022

@author: khai
"""
import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.bind((host, port))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while(True):
        print("waiting for client")
        client,  addr = sk.accept()
        print("Client address ", addr)
        #nhan du lieu
        data = client.recv(1024)            
        if not data:
            break
        s = data.decode('utf-8')
        s = s.replace(",", ", ")
        s = s.split(" ")
        res = ""
        for i in s:
            res += i.strip() + " "

        ok = 0
        s = res
        res = ""
        for i in s:
            if i == '.':
                ok = 3
            if ok == 1:
                res += i.upper()
            else:
                res += i
            if ok != 0:
                ok -= 1
        res = res.strip()     
        client.send(res.encode('utf-8'))
        client.close()
    sk.close()