#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'ZHU Guilong'


import material

from material import Resource, Machine


class NewMaterialFromFile():
    '''
    从文件生成材料；
    '''
    pass


class manager(Resource):
    pass


class engineer(Resource):
    pass


class autoclave(Machine):
    ''' 
    热压罐
    '''

    def __init__(self, name):
        self.__name = "热压罐"

        self.__state = '正常'   # 硬件是否正常，可以选项：正常、故障、报废
        self.__isReady = True  # 机器是否正常，可以选项：正常、缺少物料
        self.__isRunning = False  # 机器是否正在运行：运行中、停止中

        self.__inners = []
        self.__inners.append(inner("压缩空气", 800, 10000))     # 需要压缩空气，数字表示流量
        self.__inners.append(inner("交流电380V", 1600, 10000))   # 需要交流电

        self.__outters = []
        self.__outters.append(outter(""))         # 输出，可以为空；有可能有废气等排出；


class prepreg(material):
    ''' 
    预浸料
    '''

    def __init__(self, id):
        self.__id = id  # 型号


class inner():
    ''' 
    内部工位
    '''

    def __init__(self, filter, min, max):
        self.__filter = filter  # 定义接口能够处理的物料
        self.__minFlow = min      # 最小流量
        self.__maxFlow = max     # 最大流量，一般不起作用；


class outter():
    ''' 
    外部工位
    '''

    def __init__(self, filter, min, max):
        self.__filter = filter      # 定义接口能够处理的物料
        self.__minFlow = min         # 最小流量
        self.__maxFlow = max        # 最大流量
