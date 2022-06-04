# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:37:58 2022

@author: khai
"""

import basemodule
import socket
host = basemodule.host
port = basemodule.port

if __name__=="__main__":
    while True:
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((host, port))
            print("Connect to {}: {}".format(host, port))
            print("Enter message (q to exit):")
            msg = input()
            if(msg == 'q'):
                break
            basemodule.send_msg(sk, msg)
            print("Client gui: ", msg)
            msg = basemodule.recv_msg(sk)
            print("Server gui: ", msg)
        except ConnectionError:
            print("Error")
            break
        finally:
            sk.close()
        