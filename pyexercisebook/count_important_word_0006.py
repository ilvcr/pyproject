#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: count_important_word_0006.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月22日 星期五 16时58分31秒
#Description:  有一个目录放一个月的日记，都是 txt命名，
                    为了避免分词的问题，假设内容都是英文，
                    请统计出你认为每篇日记最重要的词。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import os
import re

def find_important_words(DirPath):
    if not os.path.isdir(DirPath):
        return
    fileList = os.listdir(DirPath)
    reObj = re.compile('\b?(\w+)\b?')
    for file in fileList:
        filePath = os.path.join(DirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
            with open(filePath) as f:
                data = f.read()
                words = reObj.findall(data)
                wordDict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a', 'the', 'to']:
                        continue
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
            ansList = sorted(wordDict.items(), key=lambda t: t[1], reverse=True)
            print 'file:{}->the most word:{}'.format(file, ansList)

if __name__ == '__main__':
    find_important_words('source/0006')



