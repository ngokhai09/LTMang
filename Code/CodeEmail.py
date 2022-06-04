# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:36:50 2022

@author: khai
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__=='__main__':
    gmail_server = "smtp.gmail.com"
    port = 465 #ssl
    from_addr = "khaingovan2001@gmail.com"
    password = "khai2001"
    to_addr = "nguyenthingu3107@gmail.com"
    message = "I love you"
    
    # Soan thao thu
    message = MIMEMultipart("alternative")
    message['Subject'] = "Test email"
    message["From"] = from_addr
    message["To"] = to_addr
    
    #tao body
    body = "This00"
    
    html ="""\
        <html>
        <body>
        <p>Hi My Love
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F82190761938655305%2F&psig=AOvVaw0Qd0fbhdKM067ra91hzpsf&ust=1644997510575000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLCcsLebgfYCFQAAAAAdAAAAABAJ">
        </p>
        </body>
        </html>
        """
    ms1 = MIMEText(html, "html")
    ms = MIMEText(body, "plain")
    message.attach(ms)
    message.attach(ms1)
    
    
    # Tạo context ssl
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(gmail_server, port, context=context)
    # Login
    server.login(from_addr, password)
    # Sau khi login viết lệnh gửi mail
    server.sendmail(from_addr, to_addr, message.as_string())
    
    
    
    
    
    
    
    
    
    
    
    # gmail_server = 'smtp.gmail.com'
    # port = 587 # starttls
    # email = "nguyenthingu3107@gmail.com"
    # password = "shmily*01"
    # to_addr = "khaingovan2001@gmail.com"
    # msg = "This is a test email"
    
    # # tao tls context
    # context = ssl.create_default_context()
    # server = smtplib.SMTP(gmail_server, port)
    # server.ehlo()
    # server.starttls(context=context)
    # server.ehlo()
    # server.login(email, password)
    # server.sendmail(email, to_addr, msg)