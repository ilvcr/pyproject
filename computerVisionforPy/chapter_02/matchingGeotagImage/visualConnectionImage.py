#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 02:29:28 PM CST
# File Name: visualConnectionImage.py
# Description:  创建一个图，该图表示深度为 2 的树，具有 5 个分支，将分支的编号添加到分支节点上
"""

import pydot

g = pydot.Dot(graph_type='graph')

g.add_node(pydot.Node(str(0), fontcolor='transparent'))
for i in range(5):
    g.add_node(pydot.Node(str(i+1)))
    g.add_edge(pydot.Edge(str(0), str(i+1)))

    for j in range(5):
        g.add_node(pydot.Node(str(j+1)+'-'+str(i+1)))
        g.add_edge(pydot.Edge(str(j+1)+'-'+str(i+1), str(j+1)))
g.write_png('graph.jpg', prog='neato')
