# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:22:25 2016
INTRODUCTION: 2: Zip file cracker - Modular
@author: Mike
"""

import zipfile

def extractFile(z_file, password):
    try:
        passwd = str.encode(password)
        z_file.extractall(pwd=passwd) # Must encode for Py3.5
        return password
    except:
        return
        
def main():  
    z_file = zipfile.ZipFile('evil.zip')
    pass_file = open('dictionary.txt')

    for line in pass_file.readlines():
        password = line.strip('\n')
        guess = extractFile(z_file, password)
        if guess:
            print('[+] Password = ' + password + '\n')
            pass_file.close()
            z_file.close()
            break # sys.exit() or 'exit(0)' throws exception. Ugly.
if __name__ == '__main__':
    main()