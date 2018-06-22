#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: find_text_HTML_0008.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月22日 星期五 17时34分40秒
#Description:   一个HTML文件，找出里面的正文。
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import requests
import re
from bs4 import BeautifulSoup

url = 'http://ilvcr.com'
data = requests.get(url)
r = re.findall(r'<body>[\s\s]*</body>', data.text)
print r[0]

print '-------------------------------------------------'
soup = BeautifulSoup(data.text, 'html.parser')
print soup.body.text



