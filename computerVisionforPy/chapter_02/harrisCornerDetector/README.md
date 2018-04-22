#Harris


##需要使用 scipy.ndimage.filters 模块中的高斯导数滤波器来计算导数。
    使用高斯滤波器的道理同样是，需要在角点检测过程中抑制噪声强度。

1-> 首先，将角点响应函数compute_harris_response添加到 harris.py 文件中，
    该函数使用高斯导数实现。同样地，参数 σ 定义了使用的高斯滤波器的尺度大小。
    也可以修改这个函数，对 x 和y 方向上不同的尺度参数，以及尝试平均操作中的不同尺度，
    来计算 Harris 矩阵。

2-> 函数compute_harris_response会返回像素值为 Harris 响应函数值的一幅图像。
    现在，需要从这幅图像中挑选出需要的信息。然后，选取像素值高于阈值的所有图像点；
    再加上额外的限制，即角点之间的间隔必须大于设定的最小距离。
    这种方法会产生很好的角点检测结果。为了实现该算法，应获取所有的候选像素点，
    以角点响应值递减的顺序排序，然后将距离已标记为角点位置过近的区域从候选像素点中删除。
    将函数get_harris_points添加到 harris.py 文件中

3-> 在有了检测图像中角点所需要的所有函数compute_harris_response, get_harris_points。
    为了显示图像中的角点，可以使用 Matplotlib 模块绘制函数plot_harris_points，
    将其添加到 harris.py 文件中

4-> Harris 角点检测器仅仅能够检测出图像中的兴趣点，但是没有给出通过比较图像间
    的兴趣点来寻找匹配角点的方法。需要在每个点上加入描述子信息，并给出一个比较这些描述子的方法

5-> 为获取图像像素块，并使用归一化的互相关矩阵来比较它们，需要另外两个函数get_descriptors, match
    将它们添加到 harris.py 文件中

6-> 函数get_descriptors的参数为奇数大小长度的方形灰度图像块，该图像块的中心为处理的像素点。
    该函数将图像块像素值压平成一个向量，然后添加到描述子列表中。
    函数match使用归一化的互相关矩阵，将每个描述子匹配到另一个图像中的最优的候选点。

7-> 由于数值较高的距离代表两个点能够更好地匹配，所以在排序之前，我们对距离取相反数。
    为了获得更稳定的匹配，我们从第二幅图像向第一幅图像匹配，然后过滤掉在两种方法中不都是最好的匹配。
    可以通过函数match_twosided实现该操作, 将它们添加到 harris.py 文件中

8-> 通过在两边分别绘制出图像，使用线段连接匹配的像素点来直观地可视化。
    可以用过函数appendimages和plot_matches实现匹配点的可视化,
    将它们添加到 harris.py 文件中

9-> 最终代码
    wid = 5
    harrisim = harris.compute_harris_response(im1,5)
    filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
    d1 = harris.get_descriptors(im1,filtered_coords1,wid)
    harrisim = harris.compute_harris_response(im2,5)
    filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
    d2 = harris.get_descriptors(im2,filtered_coords2,wid)
    print 'starting matching'
    matches = harris.match_twosided(d1,d2)
    figure()
    gray()
    harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
    show()
掉在两种方法中不都是最好的匹配
