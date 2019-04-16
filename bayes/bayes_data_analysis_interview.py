#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: bayes_data_analysis_interview.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr 16 15:13:40 2019
# Description: Using pandas handle
#************************************************************************#

import pandas as pd

class Solution(object):
    '''
        using pandas handle data
    '''
   
    def read_xlsx():
        '''
            read xlsx file's data
        '''
        names = ['agree_group', 'city_id', 'city_name', 'year', 'level', 'type', 'area', 'price', 'unit_price']
        df_land_data = pd.read_excel('land_data.xlsx', names=names)

        return df_land_data

        '''
        city_id_sort =list(sorted(set(df_land_data['city_id'])))
        '''
     def find_nan(self, df):
        '''
        judging whether there are missing values
    '''
        nan_lists = {}
        for i in df.columns:
            nan_counter = 0
            for j in df[i].isnull():
                if j:
                    nan_counter += 1
                    nan_lists[i] = nan_counter
        for k, v in nan_lists.items():
            print '{}行共有{}个缺失值'.format(k, v)

    def calc_unit_price(self, df):
        '''
            requirement 1.
        '''
        grouped_unit_price = df['unit_price'].groupby([df['city_id'], df['city_name'], df['year']])
        print grouped_unit_price.mean()

    def clac_averge_wei_price(self, df):
        '''
            requirement 2.
        '''
        grouped_price = df['price'].groupby([df['city_id'], df['city_name'], df['year']])
        grouped_area = df['area'].groupby([df['city_id'], df['city_name'], df['year']])
        print grouped_price.sum()/grouped_area.sum()




