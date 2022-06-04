# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:30:18 2022

@author: khai
"""

import basemodule

host = basemodule.host
port = basemodule.port

def client_process(sk, addr):
    try:
        # Nhan du lieu tu client
        msg = basemodule.recv_msg(sk)
        print("{} : {}".format(addr, msg))
        #gui lai client
        basemodule.send_msg(sk, msg)
    except (ConnectionError, BrokenPipeError):
        print("socket error")
    finally:
        sk.close()

if __name__=="__main__":
    sk = basemodule.create_socket(host, port)
    addr = sk.getsockname()
    print("listening on {}".format(addr))
    while True:
        client_sk, addr = sk.accept()
        print("Connection from ", addr)
        client_process(client_sk, addr)