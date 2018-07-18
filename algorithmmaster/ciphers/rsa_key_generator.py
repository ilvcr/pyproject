#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: rsa_key_generator.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 15时40分22秒
# Description: 
#************************************************************************#


from __future__ import print_function
import random
import sys
import os
import rabin_miller as rabinMiller
import cryptomath_module as cryptoMath

def main():
    print 'Making key files...'
    makeKeyFile('rsa', 1024)
    print 'Key files generation successful.'

def generateKey(keySize):
    print 'Generating prime p...'
    p = rabinMiller.generateLargePrime(keySize)
    print 'Generating prime q...'
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    print 'Generating e that is relatively prime to (p - 1) * (q - 1)...'
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p-1) * (q-1)) == 1:
            break;

    print 'Calculating d that is mod inverse of e...'
    d = cryptoMath.findModInverse(e, (p-1) * (q-1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)

def makeKeyFile(name, keySize):
    if os.path.exists('{}_pubkey.txt'.format(name)) or os.path.exists('{}_privkey.txt'.format(name)):
        print '\nWARNING:'
        print '"{}_pubkey.txt" or "{}_privkey.txt" already exists. \nUse a different \
                name or delete these files and re-run this program.'.format(name, name))
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print '\nWriting public key to file {}_pubkey.txt...'.format(name)
    with open('%s_pubkey.txt' % name, 'w') as fo:
        fo.write('{},{},{}'.format(keySize, publicKey[0], publicKey[1]))

    print 'Writing private key to file {}_privkey.txt...'.format(name)
    with open('%s_privkey.txt' % name, 'w') as fo:
        fo.write('{},{},{}'.format(keySize, privateKey[0], privateKey[1]))


if __name__ == '__main__':
    main()


