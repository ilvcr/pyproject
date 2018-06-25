#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: sen_word_0011.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月25日 星期一 21时15分34秒
#Description: 
             敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
                当用户输入敏感词语时，则打印出 Freedom，
                    否则打印出 Human Rights。

             北京
             程序员
             公务员
             领导
             牛比
             牛逼
             你娘
             你妈
             love
             sex
             jiangge

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import string

class sense_word():
    def __init__(self):
        self.list = []
        inputfile = file('filetered_word.txt', 'r')
        
        for lines in inputfile.readline():
            self.list.append(lines.decode('utf-8').encode('gbk'))
        inputfile.close()
        self.list = map(string.strip, self.list)

        for item in slef.list:
            print item

    def check_word(self, word):
        for words in self.list:
            if words == word:
                return True
        return False

if __name__ == '__main__':
    myCheck = sense_word()
    ipstr = raw_input()
    while True:
        ipstr = raw_input()
        if ipstr:
            if(myCheck.checkWord(ipstr)):
                print 'Freedom'
            else:
                print 'HumanRight'
        else:
            break


