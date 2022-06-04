# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:13:49 2022

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
    host = input("Nhap host: ")
    port = int(input("Nhap port: "))
    try:
        sk.connect((host, port))
        print("da ket noi den %s cong la %s"%(host,port))
        sk.shutdown(1)
    except socket.error as e:
        print("error")
        print("%s"%str(e))
        sys.exit()
        
    #host = input("Nhap host: ")
    # ipaddr = socket.gethostbyname(host)
    # print(ipaddr)
    # while(True):
    #     port = int(input("Nhap port: "))
    #     try:
    #         sk = socket.socket()
    #         cn = sk.connect((host, port))
    #         print("Port {0} open".format(port))
    #         sk.close()
    #     except:
    #         print("port close")
    # print("exit")
        