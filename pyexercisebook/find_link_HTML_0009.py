#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: find_link_HTML_0009.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月22日 星期五 17时38分25秒
#Description:   一个HTML文件，找出里面的链接
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import requests
import re
import os
from bs4 import BeautifulSoup

url = 'http://ilvcr.com'
data = requests.get(url)
# urls = re.findall(r'<a.*href=\"(.*?)\".*</a>',data.text)
# print(urls)

soup = BeautifulSoup(data.text, 'html.parser')
urls = soup.findAll('a')
for u in urls:
    print u['href']


