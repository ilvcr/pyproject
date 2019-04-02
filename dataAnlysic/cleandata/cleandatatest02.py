#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: cleandatatest02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 18:15:11 2019
# Description: 
#************************************************************************#

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

print "\n"
df = DataFrame(np.arange(5 * 4).reshape(5, 4))
print df
print "\n"
sampler = np.random.permutation(5)
print sampler
print "\n"
print df.take(sampler)
print "\n"
print df.take(np.random.permutation(len(df))[:3])
print "\n"

print "\n"












