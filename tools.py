# -*- coding: utf-8 -*-
# author: Bo jingqian email: jqian_bo@126.com

import socket
import fcntl
import struct
import os
import re

#配置文件路径
desktop_pwd = "/usr/share/applications/google-chrome.desktop"

#网卡
network_card = 'enp9s0'

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])

def change_desktop(ip_config,ip_now):
    lines = []
    with open(desktop_pwd,'rb') as f:
        lines = f.readlines()
    for i,_line in enumerate(lines):
        if ip_config in lines[i]:
            lines[i]=lines[i].replace(ip_config,ip_now)
            with open(desktop_pwd,'wb') as f:
                f.writelines(lines)
                break
    print "Ok~"

def old_desktop():
    ip = get_ip_address(network_card)
    with open(desktop_pwd,"rb") as f:
        content = f.read()
        ip_config = re.compile('--proxy-server="socks5://.+"').findall(content)[0]
        ip_now ='--proxy-server="socks5://%s:9999"'%ip
    return change_desktop(ip_config,ip_now)

if __name__ == '__main__':
    old_desktop()