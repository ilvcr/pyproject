#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: spider_image_0013.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月25日 星期一 21时52分16秒
#Description:   用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片
                    http://tieba.baidu.com/p/2166231880
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

import urllib2
import urllib2
import re
import os
import uuid

def get_images(html_url='http://ycool.com/post/ae3u4zu',
              folder_name='jiyou_blog_PingLiangRoad',
               extension=['gif', 'jpg', 'png']):
    request_html = urllib2.Request(html_url)

    try:
        response = urllib2.urlopen(request_html)
        html = response.read()
        r1 = r'<img.+src=\".+?\"'
        r2 = r'<img.+src=\"(.+?)\"'
        results = []
        imgs = []
        p = re.complie(r1)
        for m in p.finditer(html):
            results.append(m.group())
        for result in results:
            compile_result = re.complie(r2)
            imgs.append(compile_result.sub(r'\1', result))
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for img in imgs:
            filename = str(uuid.uuid1())
            ex = ''
            for extension in extensions:
                if '.%s' % extension in img:
                    ex = '.%s' % extension

            if ex is '':
                continue
            filename += ex
            try:
                urllib.urlretrieve(img, os.path.join(folder_name, filename))
                print 'Image save at %s' %output.name
            except Exception, ex:
                print ex
    except Exception, e:
        print e


get_images()
get_images(html_url='http://tieba.baidu.com/p/2166231880', folder_name='jp')



