#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-04-15 14:52
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : heapSort.py
 Description  :     堆排序是一种树形选择排序，是对直接选择排序的有效改进。
                1->基本思想：
                    初始时把要排序的n个数的序列看作是一棵顺序存储的二叉树（一维数组存储二叉树），
                    调整它们的存储序，使之成为一个堆，将堆顶元素输出，得到n个元素中最小(或最大)的元素，
                    这时堆的根节点的数最小（或者最大）。然后对前面(n-1)个元素重新调整使之成为堆，
                    输出堆顶元素，得到n个元素中次小(或次大)的元素。
                    依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。
                    称这个过程为堆排序。

                2->
                    实现堆排序需解决两个问题：
                    1)->如何将n 个待排序的数建成堆;
                    2.)->输出堆顶元素后，怎样调整剩余n-1 个元素，使其成为一个新堆。

                3->输出堆顶元素后，对剩余n-1元素重新建成堆的调整过程。
                    调整小顶堆的方法：
                        1)->设有m 个元素的堆，输出堆顶元素后，剩下m-1个元素。
                            将堆底元素送入堆顶（（最后一个元素与堆顶进行交换），
                            堆被破坏，其原因仅是根结点不满足堆的性质。

                        2)->将根结点与左、右子树中较小元素的进行交换。

                        3)->若与左子树交换：如果左子树堆被破坏，
                            即左子树的根结点不满足堆的性质，则重复方法（2）.

                        4)->若与右子树交换，如果右子树堆被破坏，即右子树的根结点不满足堆的性质。
                            则重复方法（2）.

                        5)->继续对不满足堆性质的子树进行上述交换操作，直到叶子结点，堆被建成。


                称这个自根结点到叶子结点的调整过程为筛选。

                4->再讨论对n 个元素初始建堆的过程。

                    建堆方法：对初始序列建堆的过程，就是一个反复进行筛选的过程。
                        1)->n 个结点的完全二叉树，则最后一个结点是第[n/2]个结点的子树。
                        2)->筛选从第[n/2]个结点为根的子树开始，该子树成为堆。
                        3)->之后向前依次对各结点为根的子树进行筛选，使之成为堆，直到根结点。

                5)->算法的实现：
                    从算法描述来看，堆排序需要两个过程，
                    一是建立堆，二是堆顶与堆的最后一个元素交换位置。所以堆排序有两个函数组成。
                    一是建堆的渗透函数，二是反复调用渗透函数实现排序的函数。
'''

lists=[49,38,65,97,76,13,27,49,55]

#选择排序—————堆排序（Heap Sort）

# 调整堆
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i

    if i < size / 2:

        if lchild < size and lists[lchild] > lists[max]:
            max =lchild

        if rchild < size and lists[rchild] > lists[max]:
            max = rchild

        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)

# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

print(heap_sort(lists))


'''
堆排序最坏情况下，时间复杂度为O(nlogn )
'''
