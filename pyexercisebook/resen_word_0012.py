#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: resen_word_0012.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月25日 星期一 21时26分01秒
#Description: 
            敏感词文本文件 filtered_words.txt，
                里面的内容 和 0011题一样，当用户输入敏感词语，
                则用 星号 * 替换，例如当用户输入「北京是个好城市」，
                    则变成「**是个好城市」。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import string

class resenseWord():
    def __init__(self):
        self.list = []
        self.word = []
        inputfile = file('filtered_words.txt', 'r')
        for lines in inputfile.readlines():
            self.list.append(lines.decode('utf-8').encode('gbk'))
        inputfile.close()
        self.list = map(string.strip, self.list)

    def checkword(self, word):
        flag = False
        for words in self.list:
            if words in word:
                self.word.qppend(words)
                flag = True
        return flag

    def genword(self):
        return flag

if __name__ == '__main__':
    myCheck = resenseWord()
    while True:
        ipstr = str(raw_input())
        if ipstr:
            if(myCheck.checkword(ipstr)):
                senseList = myCheck.getWord()
                for items in senseList:
                    length = len(items.decode('gbk'))
                    torep = '*'
                    for i in range(1, length):
                        torep = '*'
                    ipstr = ipstr.replace(items, torep)
                print ipstr
            else:
                print ipstr
        else:
            break



