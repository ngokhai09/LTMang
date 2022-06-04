# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:21:41 2022

@author: khai
"""

import basemodule
import threading

host = basemodule.host
port = basemodule.port

def xuly_client(sk, addr):
    try:
        msg = basemodule.recv_msg(sk)
        print("{},{}".format(addr, msg))
        basemodule.send_msg(sk, msg)
    except (ConnectionError, BrokenPipeError):
        print("error")
    finally:
        sk.close()

if __name__=="__main__":
    sk = basemodule.create_socket(host, port)
    addr = sk.getsockname()
    print("listening on {}".format(addr))
    while True:
        client_sk, addr = sk.accept()
        thread = threading.Thread(target=xuly_client, args=[client_sk, addr], daemon=True)
        thread.start()
        print("Connection from {}".format(addr))