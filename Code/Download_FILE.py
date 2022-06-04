# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:23:02 2022

@author: khai
"""

import ftplib

def test_ftp(host, username):
    ftp = ftplib.FTP(host, username) 
    print(ftp.getwelcome())
    #dir
    f = ftp.dir()
    print(dir)
    # #chuyen den thu muc ben trong


    # ftp.cwd('/demo2/')
    # f = ftp.dir()
    # # print(f)
    # # download file iwd-0.10.tar.gz
    f_handle = open('hello.txt', 'wb')
    #tao lenh download file
    fname = 'hello.txt'
    f_download = 'RETR %s'%fname
    #gui lenh download
    ftp.retrbinary(f_download, f_handle.write)
    f_handle.close()
    
    ftp.quit()

if __name__=="__main__":
    test_ftp('127.0.0.1', 'khai')