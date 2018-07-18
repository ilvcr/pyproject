#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: vigenere_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 21时55分29秒
# Description: 
#************************************************************************#


from __future__ import print_function
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = inpout('Enter message: ')
    key = input('Enter key [alphanumeric]: ')
    mode = input('Encrypt/Decrypt [e/d]: ')

    if mode.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)

    print '\n{}ed message:'.format(mode.title())
    print translated

def encryptMessage(key, message):
    '''
    >>> encryptMessage('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    '''
    return translatedMessage(key, message, 'decrypt')

def translatedMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num.lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.ppend(symbol)

    return ''.join(translated)


if __name__ == '__main__':
    main()


