#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: caesar_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月17日 星期二 13时00分38秒
# Description:  The Caesar Cipher Algorithm  -->>  凯撒密码算法
#************************************************************************#

from __future__ import print_function

def main():
    message = input("Enter message: ")
    key = int(input("Key [1-26]: "))
    mode = input("Encrypt or Decrypt [e/d]: ")

    if mode.lower().startswith('e'):
        mode = "encrypt"
    elif mode.lower().startswith('d'):
        mode = "decrypt"


    translated = encodec(message, key, mode)
    if mode == "encrypt":
        print(("Encrypt: ", translated))
    elif mode == "decrypt":
        print(("Decrypt: ", translated))


def encodec(message, key, mode):
    message = message.upper()
    translated = ""
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "encrypt":
                num = num + key
            elif mode == "decrypt":
                num = num -key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
            
        else:
            translated += symbol

    return translated

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()


