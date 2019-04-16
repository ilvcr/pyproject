#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: test.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr 16 18:06:19 2019
# Description: 
#************************************************************************#


names = ['agree_group', 'city_id', 'city_name', 'year', 'level', 'type', 'area', 'price', 'unit_price']
df_land_data = pd.read_excel('land_data.xlsx', names=names)

grouped_unit_price = df['unit_price'].groupby([df['city_id'], df['city_name'], df['year']])
grouped_unit_price_mean = grouped_unit_price.mean()

YEAR = [i for i in range(2006, 2018)]
for i in df['year'].groupby(df['grouped_unit_price_mean']):
    if i not in YEAR:
        result_ddillna = df.fillna(method='ffill')

print result_ddillna

'''
value_unit_price = df['grouped_unit_price_mean']
standard_data = (value_unit_price - value_unit_price.min())/ \
                (value_unit_price.max() - value_unit_price.min())

print standard_data


type_unitprice = type(df[['grouped_unit_price_mean']])
count_unitprice = type_unitprice.value_counts()

print count_unitprice
'''
