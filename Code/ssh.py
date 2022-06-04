# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:45:42 2022

@author: khai
"""

import paramiko

def test_ssh(host, port, user, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to server
    ssh.connect(host,port, user, password)
    
    # thuc hien lenh
    stdin, stdout, stderr = ssh.exec_command(command)
    sftp = ssh.open_sftp()
    localfile = ['file1.txt','file2.txt','file3.txt']
    remotefile = '/C/ProgramData/'
    for i in localfile:
        # sftp.get(remotefile + i, i)
        sftp.put(i, remotefile + i)
    sftp.close()
    # result = stdout.readlines()
    result = stdout.read().decode()
    print(result)
    
    
    
if __name__=='__main__':
    host = '127.0.0.1'
    port = 22
    user = 'ngovankhai'
    password = '2209'
    command = 'show ip in brief'
    test_ssh(host, port, user, password, command)