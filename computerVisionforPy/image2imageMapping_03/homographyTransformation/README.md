#单应性变换是将一个平面内的点映射到另一个平面内的二维投影变换。

#平面是指图像或者三维中的平面表面。单应性变换具有很强的实用性，将频繁地使用单应性变换，
#比如图像配准、图像纠正和纹理扭曲，以及创建全景图像。

#点的齐次坐标是依赖于其尺度定义的，即x=[x,y,w]=[αx,αy,αw]=[x/w,y/w,1] 都表示同一个二维点。
##因此，单应性矩阵 H 也仅依赖尺度定义，所以，单应性矩阵具有 8 个独立的自由度。
#通常使用 w=1 来归一化点，这样，点具有唯一的图像坐标 x 和 y。这个额外的坐标使得我们可以简单
##地使用一个矩阵来表示变换。

1->
    单应性矩阵可以由两幅图像（或者平面）中对应点对计算出来。
        一个完全射影变换具有 8 个自由度。根据对应点约束，每个对应点对可以写出两个方程，分别对应于 x 和 y 坐标。
            因此，计算单应性矩阵 H 需要４个对应点对。


2->
    函数normalize和make_homog可以实现对点进行归一化和转换齐次坐标的功能，将其添加到 homography.py 文件中

3->
    DLT（Direct Linear Transformation，直接线性变换）是给定４个或者更多对应点对矩阵，来计算单应性矩阵 H 的算法。
        将这些对应点对方程的系数堆叠到一个矩阵中，我们可以使用 SVD（Singular Value Decomposition，奇异值分解）
            算法找到 H 的最小二乘解。该算法使用函数H_from_points来实现，添加到 homography.py 文件中。
                函数H_from_points的第一步操作是检查点对的两个数组中点的数目是否相同。如果不相同，
                    函数将会抛出异常信息。

4->
    由于仿射变换具有 6 个自由度，因此需要三个对应点对来估计矩阵 H。通过将最后两个元素设置为 0，即 h7=h8=0，
        仿射变换可以用上面的 DLT 算法估计得出。将使用不同的方法来计算单应性矩阵 H。函数Haffine_from_points
            使用对应点对来计算仿射变换矩阵，将其添加到homograph.py 文件中。同样类似DLT 算法，
                这些点需要经过预处理和去处理化操作。


    
