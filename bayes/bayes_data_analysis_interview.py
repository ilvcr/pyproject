#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: bayes_data_analysis_interview.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr 16 19:43:40 2019
# Description: Using pandas handle land data 
#************************************************************************#

'''
Editor: vim
Run OS: Ubuntu 14.04 LTS
Python version: Python 2.7.6
pandas version: 0.22.0
'''


import pandas as pd
import re

class Solution(object):
    '''
        using pandas handle data
    '''
   
    def read_xlsx_file(self):
        '''
            read xlsx file's data
        '''
        names = ['agree_group', 'city_id', 'city_name', 'year', 'level', 'type', 'area', 'price', 'unit_price']
        
        df_land_data = pd.read_excel('land_data.xlsx', names=names)

        return df_land_data
    
    def find_NAN(self, df):
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
            print '{} 列共有{}个缺失值'.format(k, v)
    
    def calc_unit_price(self, df):
        '''
            requirement 1.
        '''
        grouped_unit_price = df['unit_price'].groupby([df['city_id'], df['city_name'], df['year']])
        
        grouped_unit_price_mean = grouped_unit_price.mean().unstack()

        return grouped_unit_price_mean

    def calc_averge_wei_price(self, df):
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
        for i in range(85):
            value_unit_price = df.iloc[i]
            
            standard_data = (value_unit_price - value_unit_price.min())/\
                            (value_unit_price.max() - value_unit_price.min())
            print standard_data
            print "\n"

    def use_type_count_unitprice(self, df):
        '''
            requirement 5.
        '''
        count_unitprice = df.groupby('type')['unit_price'].count()

        return count_unitprice

def main():
    '''
        main API
    '''
    soldata = Solution()
    
    df_land_data = soldata.read_xlsx_file()
    
    print "请注意, land_data数据表中: "
    print "********************************************************"
    soldata.find_NAN(df_land_data)
    print "********************************************************\n"

    grouped_unit_price_mean = soldata.calc_unit_price(df_land_data)

    re_float = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    
    while True:
        try:
            numbers = int(raw_input('请输入问题序号: '))
            if numbers == 1:
                print "\n每个城市每年土地成交的平均的单位价格(unit_price)为: \n"
                print grouped_unit_price_mean
        
            elif numbers == 2:
                print "\n每个城市每年土地成交的平均加权价格(sum(price)/sum(area))为: \n"
                print soldata.calc_averge_wei_price(df_land_data)
            
            elif numbers == 3:
                print "\n在1的结果上向前补全每个城市缺失年份的数据为: \n"
                print soldata.comple_unit_price_data(grouped_unit_price_mean)
            
            elif numbers == 4:
                print "\n将1中的平均单位价格标准化的结果为: \n"
                soldata.standard_aveprice(grouped_unit_price_mean)
            
            elif numbers == 5:
                print "\n按type统计unit_price的数值分布情况的结果为: \n"
                print soldata.use_type_count_unitprice(df_land_data)
            
            elif numbers.isalpha() or numbers < 0 or re_float.match(map_line):
                raise Exception
            else:
                pass
        
        except Exception as e:
            print "\n输入错误, 程序已退出, 请重新运行!"
            exit()

if __name__ == '__main__':
    main()    


