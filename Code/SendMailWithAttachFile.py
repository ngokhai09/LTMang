# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:14:25 2022

@author: khai
"""

import smtplib
import ssl
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

if __name__=='__main__':
    from_addr = "khaingovan2001@gmail.com"
    to_addr = "nguyenthingu3107@gmail.com"
    password = "khai2001"
    port = 465
    smtp_server = "smtp.gmail.com"
    
    # tao header
    message = MIMEMultipart()
    message["From"] = from_addr
    message["To"] = to_addr
    message["Subject"] = "Hello MyLove"
    message["Bcc"] = "ngkhaipv2001@gmail.com"
    
    # Tao body
    body = "I love you"
    
    # Add vao email
    message.attach(MIMEText(body, "plain"))
    
    filename = "hello.txt"
    
    #open file
    file_attach = open(filename, "rb")
    
    #add file: application/octet-stream
    attached = MIMEBase("application", "octet-stream")
    attached.set_payload(file_attach.read())
    
    # encode file -> ASCII
    encoders.encode_base64(attached)
    #add header
    attached.add_header("Content-Dispsition", f"attachment; filename={filename}")
    
    #add vao email
    message.attach(attached)
    
    # login
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, message.as_string())