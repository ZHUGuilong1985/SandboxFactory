#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. '

__author__ = 'ZHU Guilong'


from abc import ABCMeta, abstractmethod

from constant import TIME_UNIT
from enum import Enum


class MaterialUnit(Enum):
    PCS = 0
    M2 = 1
    M3 = 2
    kg = 3
    L = 4
    m = 5


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

    def get_hash_code(self, seed):  # 生产hash码
        # todo
        return 'hashcode' + seed
    
    def check_id(self):
        # check the id is legitimate or not. 

        return True


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


class SalaryType(Enum):
    MONTH = 0
    YEAR = 1
    DAY = 2
    HOUR = 3


class Worker(Resource):
    # 操作者

    def __init__(self, name,
                 id=None,
                 salary_type=SalaryType.MONTH,
                 salary=0):

        # base info
        self.typeid = MaterialType.WORKER
        self.name = name  # worker type
        if id:  # load
            if self.check_id() : # check the id is 
                return False
            self.id = id
        else:   # create
            self.id = self.get_hash_code(self.name)

        self.salary_type = salary_type
        self.salary = salary   # 工资

        #

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

    def __init__(self, name,
                 model=None,
                 support_list=None,
                 cost=0,
                 financial_life=10):

        # base info
        self.typeid = MaterialType.MACHINE
        self.name = name
        self.id = ''

        self.model = ''  # "规格型号": "6mX3mX1.5m",

        self.support_list = []  # 运维支持

        self.cost = 0  # 采购成本
        self.financial_life = 10  # 财务寿命 ,10年

        # 运维费用，根据运维支持、采购成本、财务寿命等综合自动结算。
        self.other_cost = []  # 维修成本，校验成本等等

    def report(self):
        pass


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

    def load_resource(self,resource_dict):  # 通过输入，来生产不同材料的实例；
        # with id.

        if resource_dict['typeid'] == MaterialType.MATERIAL:       # 材料
            new_resource = Material(resource_dict['name'],
                                    resource_dict['id'],
                                    resource_dict['unit'],
                                    resource_dict['price'])
        elif resource_dict['typeid'] == MaterialType.WORKER:     # 人员
            new_resource = Worker(resource_dict['name'],
                                  resource_dict['id'],
                                  resource_dict['salary_type'],
                                  resource_dict['salary'])
        elif resource_dict['typeid'] == MaterialType.MACHINE:     # 设备
            new_resource = Machine(resource_dict['name'],
                                   resource_dict['id'],
                                   resource_dict['model'],
                                   resource_dict['support_list'],
                                   resource_dict['cost'],
                                   resource_dict['financial_life'])

        return new_resource

    def create_resource(self,resource_dict):
        # without id.

        if resource_dict['typeid'] == MaterialType.MATERIAL:       # 材料
            new_resource = Material(resource_dict['name'],
                                    resource_dict['unit'],
                                    resource_dict['price'])
        elif resource_dict['typeid'] == MaterialType.WORKER:     # 人员
            new_resource = Worker(resource_dict['name'],
                                  resource_dict['salary_type'],
                                  resource_dict['salary'])
        elif resource_dict['typeid'] == MaterialType.MACHINE:     # 设备
            new_resource = Machine(resource_dict['name'],
                                   resource_dict['model'],
                                   resource_dict['support_list'],
                                   resource_dict['cost'],
                                   resource_dict['financial_life'])

        return new_resource
