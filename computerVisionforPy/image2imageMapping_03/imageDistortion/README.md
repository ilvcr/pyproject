#对图像块应用仿射变换，将其称为图像扭曲（或者仿射扭曲）。该操作不仅经常应用在计算机图形学中，
##而且经常出现在计算机视觉算法中。扭曲操作可以使用ciPy 工具包中的 ndimage 包来简单完成。
                    命令：
                            transformed_im = ndimage.affine_transform(im,A,b,size)

        使用如上所示的一个线性变换 A 和一个平移向量 b 来对图像块应用仿射变换。
            选项参数 size 可以用来指定输出图像的大小。
                默认输出图像设置为和原始图像同样大小。


#ndimage.affine_transform() 函数运行原理代码示例:(输出图像结果中丢失的像素用零来填充。)

from scipy import ndimage

im = array(Image.open('empire.jpg').convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))

figure()
gray()
imshow(im2)
show()



1->
    仿射扭曲的一个简单例子是，将图像或者图像的一部分放置在另一幅图像中，使得它们能够和指定的区域或者标记物对齐。
            将函数 image_in_image() 添加到 warp.py 文件中。该函数的输入参数为两幅图像和一个坐标。
                该坐标为将第一幅图像放置到第二幅图像中的角点坐标


2->
    在图像坐标是齐次坐标下,将扭曲的图像和第二幅图像融合后就创建了 alpha 图像。
        该图像定义了每个像素从各个图像中获取的像素值成分多少。
            基于事实，扭曲的图像是在扭曲区域边界之外以 0 来填充的图像，
                来创建一个二值的 alpha 图像。
                    严格意义上需要在第一幅图像中的潜在 0 像素上加上一个小的数值，
                        或者合理地处理这些 0 像素
      