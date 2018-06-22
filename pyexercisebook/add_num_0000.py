#!/usr/bin/env python
# coding=utf-8
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#File Name: add_num_0000.py
#Author: @Yoghourt->ilvcr, Cn,Sx,Ty
#Mail: ilvcr@outlook.com || liyaoliu@foxmail.com.com
#Created Time: 2018年06月21日 星期四 18时44分09秒
#Description:   第 0000 题：将QQ头像（或微博头像）右上角加上红色数字，类似于微信未读信息数量提示效果.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__author__ = '@yoghourt->ilvcr'

'''
from PIL import Image, ImageDraw, ImageFont

def add_num_to_img(image_path, sign="42"):
    im = Image.open(image_path)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", min(width//6, height//6))
    draw.text((width*0.75, height*0.075), sign, font=font, fill=(255, 33, 33, 255))

    left, right = image_path.rsplit(".", 1)
    new_image_path = left + "_" +sign + "." + right
    im.save(new_image_path)

if __name__ == '__main__':
    #for set
    add_num_to_img("/home/ilvcr/coding/codingpy/pyexercisebook/arial.png")
    print "Finshed"
'''

from PIL import Image, ImageDraw, ImageFont
import sys, shutil


# backup file
# @return nothing
def back_file(filename):
    p = filename.rfind('.')
    shutil.copyfile(filename, filename[:p] + '_bak' + filename[p:])


# add number to right top corner
# @return nothing
def add_number_to_image(im, num):
    xsize, ysize = im.size
    left, top = int(xsize / 20.0 * 13), int(xsize / 20.0)
    right, bottom = int(xsize / 20.0 * 19), int(xsize / 20.0 * 7)
    draw = ImageDraw.Draw(im)
    draw.ellipse([left, top, right, bottom], (255, 0, 0))
    font=ImageFont.truetype("DroidSansMono.ttf", int(xsize / 20 * 4))
    draw.text((left + xsize / 10.0, top + xsize / 30), str(num), (0, 0, 0), font=font)
    del draw


# open image and deal font and get Draw
# @return a ImageDraw
def deal(f, num):
    if (num == None):
        num = 0
    if (num > '9'):
        num = '9+'
    im = Image.open(f)
    add_number_to_image(im, num)
    im.save(f)


def main():
    if len(sys.argv) <= 1:
        print "Need at least 1 parameter."
        return
    for i in range(1, len(sys.argv), 2):
        f = sys.argv[i]
        n = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        try:
            back_file(f)
            deal(f, n)
            print "Success add number to image file", f
        except IOError:
            print "Cannot open image", f, '!'
            pass


if __name__ == '__main__':
    main()

