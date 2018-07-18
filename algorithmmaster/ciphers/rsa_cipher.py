#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: rsa_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 14时59分08秒
# Description: 
#************************************************************************#


from __future__ import print_function
import sys
import os
import rsa_key_generator as rkg

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256

def main():
    filrname = 'encrypted_file.txt'
    response = input('Encrypte\Decrypt [e\d]: ')

    if response.lower().startswith('e'):
        mode = 'encrypt'
    elif response.loer().startswith('d'):
        mode = 'decrypt'

    if mode == 'encrypt':
        if not os.path.exists('rsa_pubkey.txt'):
            rkg.makeKeyFile('rsa', 1024)

        message = input('\nEnter message')
        pubKeyFilename = 'rsa_pubkey.txt'
        print 'Encrypting and writing to {}...'.format(filename)
        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

        print '\nEncrypted text:'
        print encryptedText

    elif mode == 'decrypt':
        privKeyFilename = 'rsa_pubkey.txt'
        print 'Reading from {} and decrypting...'.format(filename)
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
        print 'writing decryption to rsa_decryption.txt...'
        with open('rsa_decryption.txt', 'w') as dec:
            dec.write(decryptedText)

        print '\nDecryption: '
        print decryptedText

def getBlocksFromText(message, blockSize = DEFAULT_BLOCK_SIZE):
    messageBytes = message.encode('ascii')

    blockInts = []

    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize-1, -1, -1):
            if len(message) + i < messageLength:
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    encrypteBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        encrypteBlocks.append(pow(block, e, n))
    
    return encrypteBlocks

def decryptMessage(encrypteBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    decryptedBlocks = []
    n, d = key
    for block in encrypteBlocks:
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)

def readKeyFile(keyFilename):
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))

def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    keySize, n, e = readKeyFile(keyFilename)
    if keySize < blockSize * 8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. \
                Either decrease the block size or use different keys.' % (blockSize * 8, keySize))

    encrypteBlocks = encryptMessage(message, (n, e), blockSize)

    for i in range(len(encrypteBlocks):
        encrypteBlocks[i] = str(encrypteBlocks[i])

    encryptedContent = ','.join(encrypteBlocks)
    encryptedContent = '{}{}{}'.format(len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    keySize, n, d = readKeyFile(keyFilename)
    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if keySize < blockSize * 8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size.\
                Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    encrypteBlocks = []
    for block in encryptMessage.split(','):
        encrypteBlocks.qppend(int(block))

    return decryptMessage(encrypteBlocks, messageLength, (n, d), blockSize)

if __name__ == '__main__':
    main()



