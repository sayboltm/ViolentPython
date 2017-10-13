# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:22:25 2016
INTRODUCTION: 2: Zip file cracker - Modular_parallelized_scriptable
@author: Mike
"""

import zipfile
import optparse
import sys
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
    #parser = optparse.OptionParser('usage%prog ' + '-f <zipfile> -d <dictionary>') # from book
    #parser = optparse.OptionParser('usage: %prog ' + '-f <zipfile> -d <dictionary>')
    #usage = 'usage: %prog [options] arg'
    #parser = optparse.OptionParser(usage)
    # This worked, not sure why it ignores first string if 'Usage: '
    parser = optparse.OptionParser('Usage: ' + 'Usage: -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        sys.exit(0)
    else:
        zname = options.zname
        dname = options.dname
        
    # Almost identical to before
    z_file = zipfile.ZipFile(zname) #
    pass_file = open(dname) #

    for line in pass_file.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(z_file, password))
        t.start()        
            
#    pass_file.close()
#    z_file.close()
# TODO: implement closing without closing before finding pw (weird...)  
if __name__ == '__main__':
    main()