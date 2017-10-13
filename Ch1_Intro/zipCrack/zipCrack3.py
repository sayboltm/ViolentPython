# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:22:25 2016
INTRODUCTION: 2: Zip file cracker - Modular_parallelized
@author: Mike
"""

import zipfile
from threading import Thread

def extractFile(z_file, password):
    try:
        passwd = str.encode(password)
        z_file.extractall(pwd=passwd) # Must encode for Py3.5
        print('[+] Found password = ' + password + '\n')
       
    except Exception as e:
        pass
        #print('Exception caught on password = ', password)
        #print(e)
        
        
def main():  
    z_file = zipfile.ZipFile('evil.zip')
    pass_file = open('dictionary.txt')

    for line in pass_file.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(z_file, password))
        t.start()        
            
#    pass_file.close()
#    z_file.close()
# TODO: implement closing without closing before finding pw (weird...)  
if __name__ == '__main__':
    main()