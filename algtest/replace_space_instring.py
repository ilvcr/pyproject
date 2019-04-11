#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: replace_space_instring.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 11:50:40 2019
# Description: 使用%20替换字符串中的空格
#************************************************************************#

class Solution(object):
    '''
        s 源字符串
    '''

    def replace_space(self, s):

        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ''
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2

        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1

        while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:

            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)


if __name__ == '__main__':
    
    s = 'daf dfer  rfeagf   fgsdgfd   fgaefga  adsfaf'
    result = Solution()
    print result.replace_space(s)

