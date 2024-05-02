#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'material mould. '

__author__ = 'ZHU Guilong'

from abc import ABCMeta, abstractmethod

from constant import TIME_UNIT
from enum import Enum

from definition import Definition


class MaterialUnit(Enum):
    PCS = 0
    M2 = 1
    M3 = 2
    kg = 3
    L = 4
    m = 5


class MaterialType(Enum):
    MATERIAL = 0
    WORKER = 1
    MACHINE = 2


class Route(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def refresh(self):
        pass


class Resource(Definition):
    '''
    元素
    工厂所有元素的基础类；
    1. 接下来，可以继承的包括，人、设备、材料等等；
    2. 材料，可以计算变质属性等动态属性；
    定义基础的属性
    '''

    def __init__(self, parent, sbid=None, name=None, description=None):
        super().__init__(parent, sbid)

        self.name = name
        self.desription = description

        self.cost = 0  # 资金

    def check_id(self):
        # check the sbid is legitimate or not.
        return True


class Material(Resource):
    '''
    材料的基础类型，可以是：材料、产品、水、电、气等
    '''

    def __init__(self, parent, sbid=None, name=None, description=None):
        super().__init__(parent, sbid)
        # unit=MaterialUnit.PCS, price=0

        # base info
        self.type_id = MaterialType.MATERIAL
        self.name = name
        self.desription = description

        self.unit = None   # 单位
        self.price = None   # 单价

    def show_info(self):
        print("Material: ", self.name,
              "unit: ",     self.unit,
              "price: ",    self.price)

    def pack_data(self):

        return {'type_id': self.type_id.value,
                'name': self.name,
                'description': self.desription,
                'sbid': self.sbid,
                'unit': self.unit.value,
                'price': self.price}


class SalaryType(Enum):
    MONTH = 0
    YEAR = 1
    DAY = 2
    HOUR = 3


class Worker(Resource):
    # 操作者

    def __init__(self, parent, sbid=None, name=None, description=None):
        super().__init__(parent, sbid)

        # base info
        self.type_id = MaterialType.WORKER
        self.name = name  # worker type
        self.desription = description

        # local info
        self.salary_type = SalaryType.MONTH  # 工资类型
        self.salary = 0     # 工资
        self.consume = ""   # 消耗，佣金
        self.costs = ""     # 保留工资

        self.sub_resource = []  #
        self.vssel = None       #

    def show_info(self):
        print("Worker: ",       self.name,
              " sbid: ",        self.sbid,
              " salary: ",      self.salary,
              " salary_type: ", self.salary_type)

    def pack_data(self):
        return {'type_id': self.type_id.value,
                'name': self.name,
                'description': self.desription,
                'sbid': self.sbid,
                'salary_type': self.salary_type.value,
                'salary': self.salary,
                'consume': self.consume,
                'costs': self.costs}


class Machine(Resource):
    '''
    设备
    '''

    def __init__(self, parent, sbid=None, name=None, description=None):
        # self, name, model=None, support_list=None, cost=0, financial_life=10
        super().__init__(parent, sbid)

        # base info
        self.type_id = MaterialType.MACHINE
        self.name = name
        self.desription = description

        # local info
        self.manufacturer = None    # 制造商
        self.model = ''             # "规格型号": "6mX3mX1.5m"

        # supports: dicts, {"obj": obj, "qty": qty, '_description': _description}
        self.support_list = []
        self.cost = 0               # 采购成本
        self.financial_life = 10    # 财务寿命 ,10年
        # 运维费用，根据运维支持、采购成本、财务寿命等综合自动结算。
        self.other_cost = []  # 维修成本，校验成本

    def show_info(self):
        print("Machine: ", self.name, " sbid: ", self.sbid)

    def pack_data(self):
        return {'type_id': self.type_id.value,
                'name': self.name,
                'description': self.desription,
                'sbid': self.sbid,
                'manufacturer': self.manufacturer,
                'model': self.model,
                'support_list': self.support_list,
                'cost': self.cost,
                'financial_life': self.financial_life,
                'other_cost': self.other_cost}


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

    def __init__(self, root):
        self.root = root    # 容器

    def load_resource(self, resource_dict):  # 通过输入，来生产不同材料的实例；
        # with sbid.

        if resource_dict['type_id'] == MaterialType.MATERIAL.value:  # 材料
            new_resource = Material(self.root,
                                    resource_dict['sbid'],
                                    resource_dict['name'])
            new_resource.price = resource_dict['price']
            new_resource.unit = resource_dict['unit']

        elif resource_dict['type_id'] == MaterialType.WORKER.value:  # 人员
            new_resource = Worker(self.root,
                                  resource_dict['sbid'],
                                  resource_dict['name'])
            new_resource.salary = resource_dict['salary']
            new_resource.salary_type = resource_dict['salary_type']

        elif resource_dict['type_id'] == MaterialType.MACHINE.value:  # 设备
            new_resource = Machine(self.root,
                                   resource_dict['sbid'],
                                   resource_dict['name'])

            new_resource.price = resource_dict['price']
            new_resource.unit = resource_dict['unit']

            # resource_dict['model']
            # resource_dict['support_list']
            # resource_dict['cost']
            # resource_dict['financial_life']

        return new_resource

    def create_resource(self, resource_dict):
        # without sbid.

        if resource_dict['type_id'] == MaterialType.MATERIAL:  # 材料
            new_resource = Material(resource_dict['name'],
                                    resource_dict['unit'],
                                    resource_dict['price'])
        elif resource_dict['type_id'] == MaterialType.WORKER:  # 人员
            new_resource = Worker(resource_dict['name'],
                                  resource_dict['salary_type'],
                                  resource_dict['salary'])
        elif resource_dict['type_id'] == MaterialType.MACHINE:  # 设备
            new_resource = Machine(resource_dict['name'],
                                   resource_dict['model'],
                                   resource_dict['support_list'],
                                   resource_dict['cost'],
                                   resource_dict['financial_life'])

        return new_resource


def main():
    pass


if __name__ == '__main__':
    # 测试代码
    factory = ResourceFactory()
