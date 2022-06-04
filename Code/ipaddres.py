# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:59:40 2022

@author: khai
"""

import ipaddress as ip
if __name__=="__main__":
    ipaddr = ip.network('10.0.1.0/24')
    ipaddr = ip.ip_network('10.0.1.0/24')
    ipaddr.netmask
    str(ipaddr.netmask)
    str(ipaddr.network_address)
    str(ipaddr.broadcast_address)
    ipaddr.num_addresses