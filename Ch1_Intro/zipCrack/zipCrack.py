# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:22:25 2016
INTRODUCTION: 2: Zip file cracker
@author: Mike
"""

import zipfile
import sys

z_file = zipfile.ZipFile('evil.zip')
pass_file = open('dictionary.txt')

for line in pass_file.readlines():
    password = line.strip('\n')
    try:    
        passwd = str.encode(password)
        z_file.extractall(pwd=passwd) # Must encode for Py3.5
        print('[+] Password = ' + password + '\n')
        pass_file.close()
        z_file.close()
        #sys.exit()
        break # sys.exit() or 'exit(0)' throws exception. Ugly.
    except Exception as e:
        #print(e)
        pass