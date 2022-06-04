# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:22:26 2022

@author: khai
"""

import imaplib
import getpass

GOOGLE_IMAP_SERVER = "imap.googlemail.com"
IMAP_SERVER_PORT = "993"
def FetchEmail(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select("Inbox")
    tmp, data = mailbox.search(None, "ALL")
    for index in data[0].split():
        tmp, data = mailbox.fetch(index, '(RFC822)')
        print("Message: ", index)
        print(data[0][1])
        break
    mailbox.close()
    mailbox.logout()

if __name__=="__main__":
    username = "khaingovan2001@gmail.com"
    password = getpass.getpass(prompt="Enter your email password: ")
    FetchEmail(username, password)