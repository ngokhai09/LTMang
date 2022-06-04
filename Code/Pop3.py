# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:02:59 2022

@author: khai
"""

import poplib
import getpass

GOOGLE_POP3_SERVER = "pop.googlemail.com"
POP3_SERVER_PORT = "995"
def FetchEmail(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, POP3_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    numMess = len(mailbox.list()[1])
    print("Total emails: ", numMess)
    print("Getting last message: ")
    for msg in mailbox.retr(numMess):
        print(msg)
    mailbox.quit()
    
if __name__=="__main__":
    username = "khaingovan2001@gmail.com"
    password = getpass.getpass(prompt="Enter your email password: ")
    FetchEmail(username, password)