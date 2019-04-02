#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testtwodim.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Sat Mar 30 11:13:59 2019
# Description: 
#************************************************************************#


L = "GRFFFGFFGDGFFGRFGFGRFGRG"

M = []
LL = list(L)
print LL

for i in range(0, len(L), 6):
    M.append(L[i:i+6])
print M

for i in range(len(M)):
    for j in range(len(M[0])):
        if j % 2 == 1:
            M[i] = M[i][::-1]
            if M[i][j] == 'D':
                M[i] = M[i][:j-1] + 'W' + M[i][j] + 'W' + M[i][j+2:]
                M[i-1] = M[i-1][:j-1] + 'WWW' + M[i-1][j+2:]
                M[i+1] = M[i+1][:j-1] + 'WWW' + M[i+1][j+2:]
                for i in range(len(M)):
                    print M[i]



