#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: transpostion_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 21时45分02秒
# Description: 
#************************************************************************#

from __future__ import print_function
import math

def main():
    message = input('Enter message: ')
    key = int(input('Enter key [2-%s]: ' % (len(message) - 1)))
    mode = input('Encryption/Decryption [e/d]: ')

    if mode.lower().startswith('e'):
        text = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        text = decryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print 'Output:\n{}'.format(text = '|'))

def encryptMessage(key, message):
    """
    >>> encryptMessage(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """

    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

def decryptMessage(key, message):
    """
    >>> decryptMessage(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    numCols = math.ceil(len(mesage) / key)
    numRows = key
    numShadeBoxes = (numCols * numRows) - len(message)

    plainText = [""] * numCols
    col = 0
    row = 0

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if(col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()


