# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:35:18 2023

@author: omen
"""

# 返回上一次更新数据库的日期（时间戳）
def get_database_last_updated():
    return 100000

# 返回上一次更新数据分析结果的日期（时间戳）
def get_analyse_last_updated():
    return 1687604017.4140306

# 把上一次更新数据库的日期（时间戳）存入数据库
def set_database_last_updated(time):
    print("设置数据库最后更新时间")
    
# 把上一次更新数据分析结果的日期（时间戳）存入数据库
def set_analyse_last_updated(time):
    print("设置数据分析结果最后更新时间")
   