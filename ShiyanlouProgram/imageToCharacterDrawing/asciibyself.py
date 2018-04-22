#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 03 Apr 2018 09:48:16 PM CST
# File Name: asciibyself.py
# Description:
"""

from PIL import Image
import argparse #argparse 库是用来管理命令行参数输入

#命令行输入参数处理
parser = argparse.ArgumentParser()

#输入文件
parser.add_argument("file")
#输出文件
parser.add_argument('-o', '--output')
#输出字符画宽
parser.add_argument('--width', type = int, default = 80)
#输出字符画高
parser.add_argument('--height', type = int, default = 80)

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#以下是字符画所使用的字符集，一共有70个字符，字符的种类与数量可根据字符画的效果反复调试
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


#定义RGB值转字符的函数,将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ''

    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

if __name__ == "__main__":
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += "\n"

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
