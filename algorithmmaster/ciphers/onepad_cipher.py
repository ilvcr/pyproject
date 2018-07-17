#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: onepad_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月17日 星期二 13时18分31秒
# Description: 
#************************************************************************#


class Onepad(object):
    def encrypt(self, text):
        '''Function to encrypt text using psedo-random numbers'''
        plain = []
        key = []
        cipher = []

        for i in text:
            plain.append(ord(i))

        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)

        return cipher, key

    def decrypt(self, cipher, key):
        '''Function to decrypt text using psedo-random numbers.'''
        plain = []
        for i in range(len(key)):
            p = (cipher[i] - (key[i])**2) / key[i]
            plain.append(chr(p))
        plain = ''.join([i for in plain])
        return plain

if __name__ == '__main__':
    c, k = Onepad().encrypt('Hello')
    print c, k
    print Onepad().decrypt(c, k)


