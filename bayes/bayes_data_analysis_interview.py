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
import numpy as np


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
        grouped_unit_price_mean = grouped_unit_price.mean().unstack()

        return grouped_unit_price_mean

    def clac_averge_wei_price(self, df):
        '''
            requirement 2.
        '''
        grouped_price = df['price'].groupby([df['city_id'], df['city_name'], df['year']])
        grouped_area = df['area'].groupby([df['city_id'], df['city_name'], df['year']])
        average_weight_price = grouped_price.sum()/grouped_area.sum()
        
        return average_weight_price

    def comple_unit_price_data(self, df):
        '''
            requirement 3.
        '''
        result_ddillna = df.fillna(method='ffill')

        return result_ddillna

    def standard_aveprice(self, df):
        '''
            requirement 4.
        '''
        value_unit_price = df['grouped_unit_price_mean']
        standard_data = (value_unit_price - value_unit_price.min())/ \
                        (value_unit_price.max() - value_unit_price.min())
        
        return standard_data

    def use_type_count_unitprice(self, df):
        '''
            requirement 5.
        '''
        type_unitprice = type(df[['grouped_unit_price_mean']])
        count_unitprice = type_unitprice.value_counts()

        return count_unitprice


if __name__ == '__main__':
    soldata = Solution()


