#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. '

__author__ = 'ZHU Guilong'


from abc import ABCMeta, abstractmethod

from constant import TIME_UNIT
from enum import Enum


class MaterialUnit(Enum):
    PCS = 0


class MaterialType(Enum):
    WORKER = 0
    MACHINE = 1
    MATERIAL = 2


class Route(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def refresh(self):
        pass


class Resource:
    '''
    元素
    工厂所有元素的基础类；
    1. 接下来，可以继承的包括，人、设备、材料等等；
    2. 材料，可以计算变质属性等动态属性；
    定义基础的属性
    '''

    resource_list = []  # 总的元素列表

    def __init__(self):

        self.name = ''
        self.id = None  # 用hash码解决id唯一的问题

        self.resource_list.append(self)  # 加入到列表
        self.is_working = True

    def update(self):
        pass

    def report(self):
        print("I'm running! ")


class Material(Resource):
    ''' 
    材料的基础类型
    可以是：材料、产品、水、电、气等；
    '''

    def __init__(self,
                 name,
                 unit=MaterialUnit.PCS,
                 price=0):

        # base info
        self.typeid = MaterialType.MATERIAL    
        self.id = ''    # auto created
        self.name = name
        self.unit = unit   # 单位
        self.price = price   # 单价

        self.is_work = None     #
         


class Worker(Resource):
    # 操作者

    def __init__(self, name):

        self.__name = name  # worker type
        self.id = ''

        self.consume = ""   # 消耗，佣金
        self.costs = ""     # 保留工资
        self.sub_resource = []  #
        self.vssel = None       #

        self.is_work = True      # 是否正常工作

        print(f'Worker {name} is created. ')

    def update(self):
        pass


class Machine(Resource):
    '''
    设备
    '''

    def __init__(self, name):
        self.__name = name
        self.__id = ""

        self.__energyConsumption = 0
        self.__energy = "压缩空气"

        self.report()  # 报告

    def report(self):
        print(self.__name)


class MaterialOperator:
    '''
    材料操作器，主要功能：
    1. 材料的分切；
    2. 材料的合并；
    3. 材料的销毁；

    材料可以分为：
    拆分，指的是小数；
    1. 可拆分的连续材料，如水、燃气等等；单位，kg、m³等
    2. 不可拆分的连续材料X
    3. 可拆分的离散材料；X
    4. 不可拆分的离散材料
    5. 数量强制为1的材料，即单件材料；
    不可拆分，如卷、件。解决卷料的问题；
    3. 只能为单件的材料，如设备、人员等，因为不可能有相同的人、设备。要记录不同的属性；

    问题：
    1. 如何解决材料动态问题？
    2. 如何解决材料变质问题

    配置，通过配置来定义材料；
    材料的大类，是通过类来定义的；
    '''
    pass


class ResourceFactory:

    def __init__(self):
        pass

    def new_resource(resource_dict):  # 通过输入，来生产不同材料的实例；

        if resource_dict['typeid'] == 1:       # 材料
            new_resource = Material(resource_dict['name'], 
                                    resource_dict['unit'], 
                                    resource_dict['price']) # 区分新建和导入
        elif resource_dict['typeid'] == 2:     # 人员
            new_resource = Worker(resource_dict['name'])
        elif resource_dict['typeid'] == 3:     # 设备
            new_resource = Machine(resource_dict['name'])

        return new_resource


class Inner():
    # 内部工位
    def __init__(self, filter, min, max):
        self.__filter = filter      # 定义接口能够处理的物料
        self.__minFlow = min        # 最小流量
        self.__maxFlow = max        # 最大流量，一般不起作用；


class Outter():
    ''' 
    外部工位
    '''

    def __init__(self, filter, min, max):
        self.__filter = filter          # 定义接口能够处理的物料
        self.__minFlow = min            # 最小流量
        self.__maxFlow = max            # 最大流量
