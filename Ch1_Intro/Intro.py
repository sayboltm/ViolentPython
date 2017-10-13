# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:27:33 2016
CHAPTER 1: Introduction
@author: Mike
"""
import socket

#### NETWORKING ####
socket.setdefaulttimeout(2)
s = socket.socket()
#s.connect(('192.168.95.148',21))
#ans = s.recv(1024)
#print(ans)

#if ('FreeFloat Ftp Server (Version 1.00)' in ans):
#    print('[+] FreeFloat FTP Server is fulerable.')
#else:
#    print('[-] FreeFloat FTP Server is not vulnerable.')
    
    
#### EXCEPTION HANDLING ####
try:
    print('[+] 1337/0 = '+str(1337/0))
#except:
#    print('[-] Error.')
except Exception as e: # Differs from V2.7
    print('[-] Test Error = '+str(e))
    
    
#try:
#    s.connect(('192.168.95.148',21))
#except Exception as e:
#    print('[-] Error = '+str(e))
    
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
        
def checkVulns(banner):
    if ('FreeFloat Ftp Server (Version 1.00)' in ans):
        print('[+] FreeFloat FTP Server is fulerable.')
    else:
        print('[-] FreeFloat FTP Server is not vulnerable.')
    return

def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '192.168.95.150'
    port = 21
    port_list = [21,22,25,80,110]
    
    banner1 = retBanner(ip1, port)
    if banner1:
        print('[+] ' + ip1 + ': ' + banner1)
        checkVulns(banner1)
        
    banner2 = retBanner(ip2, port)
    if banner2:
        print('[+] ' + ip2 + ': ' + banner2)
        checkVulns(banner2)
        
    
    banner3 = retBanner(ip3, port)
    if banner2:
        print('[+] ' + ip3 + ': ' + banner3)
        checkVulns(banner3)
        
    
    for x in range(1,255):
        for port in port_list:
            print('[+] Checking 192.168.95.'+str(x)+':'+str(port))
        
if __name__ == '__main__':
    main()