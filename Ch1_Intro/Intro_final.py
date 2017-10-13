# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:27:33 2016
CHAPTER 1: Introduction
@author: Mike
"""
import socket
import os
import sys
    
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print('[-] Program shit bricks inside retRanner('+ip+', '+str(port)+') with exception: '+str(e))        
        return
        
def checkVulns(banner):
    f = open(filename, 'r')
    for line in f.readlines():    
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable: ' + banner.strip('\n'))
        else:
            print('[-] FreeFloat FTP Server is not vulnerable.')

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print ('[-] ' + filename + ' does not exist')
            sys.exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] ' + filename + ' access denied.')
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
        sys.exit(0)
        
    port_list = [21,22,25,80,110,443]
    
    for x in range(147,150):
        ip = '192.168.95.' + str(x)
        for port in port_list:
            banner = retBanner(ip, port)
            if banner:
                print('[+] ' + ip + ':' + banner)
                checkVulns(banner, filename)
        
if __name__ == '__main__':
    main()