#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'蓝图模块'

__author__ = 'ZHU Guilong'

from enum import Enum

import blueprint_mould
from constant import TIME_UNIT

DEFAULT_BLUEPRINT = "复合材料工厂"
DEFAULT_BLUEPRINT2 = {



}


class Blueprint():
    '''
    车间蓝图：
    1. 适用于工段、车间和工厂
    '''

    def __init__(self, blueprint_name, blueprint_txt):
        self.__blueprint_name = blueprint_name  # "复合材料工厂"
        self.__blueprint_txt = blueprint_txt
        self.__objectlinklist = []              # 空表

    def fatmat(self):
        '''
        格式化公式
        '''
        pass

    def translation(self):
        ''' 
        翻译，转译文本成对象
        '''
        self.__objectlinklist.append(objectlink())  # element links, - todo

    def check(self):
        '''
        检查
        1. 不要存在孤点
        '''
        return True

    def resetPointer(self):
        ''' 
        设置指针
        '''
        self.__pointer = 0
        pass

    def get_next_link(self):
        ''' 
        获取下一个链接
        '''
        if self.__pointer != 0:
            return self.__objectlinklist[self.__pointer]

        return None


class BlueprintFactory():
    pass

    def __init__(self):
        pass

    def new_blueprint(self, blueprint_str):
        # 根据提供的字典，创建类

        return Blueprint()
