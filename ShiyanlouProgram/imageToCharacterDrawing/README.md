1->字符画是一系列字符的组合，可以把字符看作是比较大块的像素，一个字符能表现一种颜色（暂且这么理解吧），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。

2->要转换一张彩色的图片，许多的颜色，要怎么对应到单色的字符画上去？这里就要介绍灰度值的概念了。

3->灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像


4->可以使用灰度值公式将像素的 RGB 值映射到灰度值：

                                                      gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

5->可以创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。
