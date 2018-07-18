#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: xor_cipher.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月18日 星期三 22时08分13秒
# Description: 
    This class implements the XOR-cipher algorithm and provides some 
    useful methods for encrypting and decrypting strings and files.

    Overview about methods

    - encrypt : list of char
    - decrypt : list of char
    - encrypt_string : str
    - decrypt_string : str
    - encrypt_file : boolean
    - decrypt_file : boolean
#************************************************************************#

class XORcipher(object):
    def __init__(self, key = 0):
        """
        simple constructor that receives a key or uses
        default key = 0
        """

        #private field
        self.__key = key

    def encrypt(self, content, key):
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert(isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        #make sure key can be any size
        while key > 255:
            key -= 255

        #This will be returned
        ans = []

        for ch in content:
            ans.append(chr(ord(ch)^key))

        return ans

    def decrypt(self, content, key):
        """
        input: 'content' of type list and 'key' of type int
        output: decrypted string 'content' as a list of chars
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert(isinstance(key, int) and isinstance(content, list))

        key = key or self.__key or 1

        #make sure key can be any size
        while key > 255:
            key -= 255

        #This will be returned
        ans = []

        for ch in content:
            ans.append(chr(ord(ch)^key))

        return ans


    def encrypt_string(self, content, key = 0):
        """
        input: 'content' of type string and 'key' of type int
        output: encrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert (isinstance(key,int) and isinstance(content,str))

        key = key or self.__key or 1
        
        # make sure key can be any size
        
        while (key > 255):
            key -= 255
        
        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans


    def decrypt_string(self, content. key = 0):
        """
        input: 'content' of type string and 'key' of type int
        output: decrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """
        
        # precondition
        assert (isinstance(key,int) and isinstance(content,str))

        key = key or self.__key or 1
        
        # make sure key can be any size
        while (key > 255):
            key -= 255

        # This will be returned
        ans = ""
                                                                                                                                                
        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file, key = 0):
        """
        input: filename (str) and a key (int)
        output: returns true if encrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
	"""
        
        #precondition
	assert (isinstance(file,str) and isinstance(key,int))
        
        try:
            with open(file,"r") as fin:
                with open("encrypt.out","w+") as fout:

                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.encrypt_string(line,key))
	except:
            return False

	return True
    
    def decrypt_file(self,file, key):
        """
        input: filename (str) and a key (int)
        output: returns true if decrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

    	#precondition
        assert (isinstance(file,str) and isinstance(key,int))

	try:
            with open(file,"r") as fin:
                with open("decrypt.out","w+") as fout:

                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.decrypt_string(line,key))

	except:
            return False
        
        return True


