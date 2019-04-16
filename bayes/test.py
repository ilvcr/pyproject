#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: test.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr 16 18:06:19 2019
# Description: 
#************************************************************************#

import pandas as pd

names = ['agree_group', 'city_id', 'city_name', 'year', 'level', 'type', 'area', 'price', 'unit_price']
df_land_data = pd.DataFrame(pd.read_excel('land_data.xlsx', names=names))
#df_land_data_ = pd.read_excel('land_data.xlsx', names=names)
#print df_land_data[:10]
#print df_land_data_[:10]


grouped_unit_price = df_land_data['unit_price'].groupby([df_land_data['city_id'], df_land_data['city_name'], df_land_data['year']])
grouped_unit_price_mean = grouped_unit_price.mean().unstack()
#print grouped_unit_price_mean[20:30]

'''
result_ddillna = grouped_unit_price_mean.fillna(method='ffill')
#print result_ddillna

'''

for i in range(85):
    value_unit_price = grouped_unit_price_mean.iloc[i]
    #print value_unit_price
    standard_data = (value_unit_price - value_unit_price.min())/(value_unit_price.max() - value_unit_price.min())
    #standard_data = pd.
    print '\n'
    print standard_data
    
    #dict_standard_data = pd.DataFrame({'year':standard_data.index, 'data':standard_data.values}, columns=['year', 'data'])
    #print dict_standard_data


'''
count_unitprice = df_land_data.groupby('type')['unit_price'].count()
print count_unitprice
'''



