#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: simple_substitution_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 21时16分05秒
# Description: 
#************************************************************************#

from __future__ import print_function
import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('Enter message: ')
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    resp = input('Encrypt/Decrypt [e/d]: ')

    checkVaildKey(key)

    if resp.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif resp.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)

    print '\n{}ion: \n{}'.format(mode.title(), translated)
    #new future
    #print(F'\n{mode.title()}ion: \n{translated}')

def checkVaildKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    if keyList != lettersList:
        sys.exit('Error in the key or symbol set.')

def encryptMessage(key, message):
    """
    >>> encryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charB[symIndex].lower()
        else:
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__;:
    main()


