#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: transposition_cipher_encryptdecrypt_file.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 21时34分01秒
# Description: 
#************************************************************************#


from __future__ import print_function
import time
import os
import sys
import transposition_cipher as transCipher

def main():
    inputFile = 'Prehistoric Men.txt'
    outputFile = 'Output.txt'
    key = int(input('Enter key: '))
    mode = input('Encrypt/Decrypt [e/d]: ')

    if not os.path.exists(inputFile):
        print 'File {} does not exist. Quitting...'.format(inputFile)
        sys.exit()
    if os.path.exists(outputFile):
        print 'Overwrite {}? [y/n]'.format(outputFile)
        response = input('> ')
        if not response.lower().startswith('y'):
            sys.exit()

    startTime = time.time()
    if mode.lower().startswith('e'):
        content = open(inputFile).read()
        translated = transCipher.encryptMessage(key, content)
    elif mode.lower().startswith('d'):
        content = open(outputFile).read()
        translated = transCipher.DecryptMessage(key, content)


    outputObj = open(outputFile, 'w')
    outputFile.write(translated)
    outputObj.close()

    totalTime = round(time.time() - startTime, 2)
    print ('Done(', totalTime, 'seconds )')


if __name__ == '__main__':
    main()


