# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:14:15 2023

@author: omen
"""
import time
from src.config import *

#from analyse import analyseInterface
from src.exhibition.exhibitionInterface import exhibit 
from src.database_manager.databaseManagerInterface import *


# 更新数据库
def update_database():
    current_tick = time.time()
    
    print("当前时间戳",current_tick)
    print("上次数据库更新时间戳",get_database_last_updated())
    print("数据库更新间隔",database_update_interval)
    
    if current_tick - get_database_last_updated() > database_update_interval:
        print ("更新数据库")
        set_database_last_updated(time.time())
    else:
        print("不用更新数据库")

# 更新数据分析结果
def update_analyse():
    current_tick = time.time()
    
    print("当前时间戳",current_tick)
    print("上次分析结果更新时间戳",get_analyse_last_updated())
    print("分析结果更新间隔",analyse_update_interval)
    
    if current_tick - get_analyse_last_updated() > analyse_update_interval:
        print ("更新分析结果")
        set_analyse_last_updated(time.time())
    else:
        print("不用更新分析结果")


# 数据展示页面
def visibility():
    print("数据展示页面")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    update_database()
    update_analyse()
    visibility()
    
    
