# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:37:22 2022

@author: khai
"""

import smtplib
import ssl
import csv

if __name__=='__main__':
    from_addr = "khaingovan2001@gmail.com"
    to_addr = "nguyenthingu3107@gmail.com"
    password = "khai2001"
    port = 465
    smtp_server = "smtp.gmail.com"
    
    message = """Subject: Luong thang
    Xin chao {hoten}, luong cua ban la {luong}"""
    
    # login
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(from_addr, password)
    
    # Gui email
    filecsv = open("test.csv")
    data = csv.reader(filecsv)
    next(data) #bo qua header
    for hoten, email, luong in data:
        server.sendmail(from_addr, email, message.format(hoten=hoten, luong=luong))