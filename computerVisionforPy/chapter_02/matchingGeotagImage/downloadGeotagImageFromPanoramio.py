#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 02:05:59 PM CST
# File Name: downloadGeotagImageFromPanoramio.py
# Description:  从Panoramio下载地理标记图像
                    将使用 Python 里的 urllib 工具包来处理请求，然后使用 simplejson 工
                    具包解析返回结果
"""

import os
import urllib, urlparse
import simplejson as json

#查询图像
url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&\
        set=public&from=0&to=20&minx=-77.037564&miny=38.896662&\
        maxx=-77.035564&maxy=38.898662&size=medium'

c = urllib.urlopen(url)

#从JSON中获得每个图像的url
j = json.loads(c.read())
imurls = []
for im in j['photos']:
    imurls.append(im['photo_file_url'])

#下载图像
for url in imurls:
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
    print("DOWNLOADING:", url)

