#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
  Author       : Yoghourt.Lee->lvcr
  Last modified: 2018-04-11 22:39
  Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
  Filename     : searchExDangD.py
  Description  : 在一个文件内搜索指定内容的数量
'''


import codecs
'''
用codecs提供的open方法来指定打开的文件的语言编码,
它会在读取的时候自动转换为内部的unicode
'''
'''
第一步
import codecs
filepath=r"FILEPATH\FILENAME"

file=codecs.open(filepath,"rb",encoding="gbk",errors="ignore")
for  line  in  file:#硬盘模式
    print(line)
'''
def  loaddata():		#加载数据
    filepath = r"FILEPATH\FILENAME"		#文件路径
    file = codecs.open(filepath, "rb", encoding="gbk", errors="ignore")		#文件打开方式
    global datalist 		#引用全局
    datalist=file.readlines() 		#读取文件到list
    file.close()		关闭文件
def  search(namestr):
    savefilepath="FILEPATHSAVE"+namestr+".txt"		#盘符:\\第一层文件名\\第二层文件名\\第三层文件名\\第四层文件名\\...
    savefile=open(savefilepath,"wb")		#文件路径
    numbers=0		#number 为计数器
    for  line  in datalist:		#迭代
        if line.find(namestr)!= -1:		#判断条件
            print(line,end="") 		#显示数据
            numbers +=1
            savefile.write(line.encode("utf-8"))		#写入
    savefile.write(("数量"+str(numbers)).encode("utf-8"))
    savefile.close()


datalist=[]
print("load  file start")
loaddata()
print("load  file end")
while True:
    searchname=input("要查询的数据")
    search(searchname)