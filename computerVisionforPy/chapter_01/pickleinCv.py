#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 03:29:03 PM CST
# File Name: pickleinCv.py
# Description:  Python中的pickle 模块可以接受几乎所有的 Python 对象，
                    并且将其转换成字符串表示，该过程叫做封装（pickling）。
                    从字符串表示中重构该对象，称为拆封（unpickling）。
                    这些字符串表示可以方便地存储和传输。

                    代码功能：
                            对图像的平均图像和主成分的处理
"""

#保存均值和主成分数据
f = open('font_pca_modes.pk1', 'wb')
pickle.dump(imean, f)
pickle.dump(V, f)
f.close()
'''
pickle 模块中有很多不同的协议可以生成 .pkl 文件；
如果不确定，最好以二进制文件的形式读取和写入。
'''

#载入均值和主成分数据
f = open('font_pca_modes.pk1', 'rb')
immean = pickle.load(f)
V = pickle.load(f)
f.close()

'''
#上下文管理器方法

#打开文件并保存
with open('font_pca_modes.pk1', 'wb') as f:
    pickle.dump(immean, f)
    pickle.dump(V, f)

#打开文件并载入
with open('font_pca_modes.pk1', 'rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)

