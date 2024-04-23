#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. 定义具体的材料、设备、人员等等，相当于Excel表格。'

__author__ = 'ZHU Guilong'

from constant import TIME_UNIT
from enum import Enum


# class LogicType(Enum):

#     NEW = 1             # 发生器 +
#     MANUFACTURE = 2     # 制造
#     RECYCLE = 3         # 回收 -
#     TRANSPORT = 4       # 传送 ->
#     STORAGE = 5         # 存储 =
#     CHANNEL = 6         # 多通道


# class ItemsType(Enum):
#     IN = 1
#     HOLD = 2
#     OUT = 3


class MaterialPosition:
    def __init__(self, tp, material_name, num):

        self.material_name = material_name

        # self.filter = filter  # 过滤器，实际上就是材料名称；
        self.num = num
        self.type_material = tp  # in, out, hold, other
        # self.speed = 20


class Formula():
    '''
    典型配方：
    1. support:     machine1,   需要电  , worker1,    需要现金；
    2. input:         inner1，        inner2，
    3. output:         outter1,         outter2, 

    3. 过程

    (in station2): 材料1 x20 + 材料2 x 12 -(5min x 12，可暂停)-> 产品1 x2 +废弃物2 x3

    适用于station：

    内部逻辑关系梳理：
    1. 硬件需要能量输入，运行；
    配置工位：
    1. station ID
    2. station Name
    3. equipments
    4. workers
    5. toolings
    有一个基础能耗，基础的启动前置时间，完成后置时间；
    '''

    def __init__(self,
                 name,
                 id=None,
                 str_formula=None):
        # str_formula, dict

        self.name = name
        self.id = id


        self.support = []   # 电力
        self.input = []     # 输入
        self.output = []    # 输出
        self.matching_table = []   # 匹配表，传送装置才会有。
        self.time = str_formula["time"]
        self.can_pause = str_formula["canPause"]


    def add_input(self, dict):
        # 增加一条输入
        self.input.append(dict)

    def add_output(self, dict):
        self.output.append(dict)

    def add_support(self, dict):
        self.support.append(dict)

    def add_matching_table(self, dict):
        self.matching_table(dict)

    def set_input(self, lst):
        # 设置所有输入
        self.add_input.clear()  # 清空
        for item in lst:
            self.add_input(item)

    def set_output(self,lst):
        pass

    def set_support(self,lst):
        pass

    def set_matching_table(self, lst):
        pass

    def translation(self):
        pass


class FormulaFactory:

    def load_formula(self, formula_dict):  # 通过输入，来生产公式实例

        new_formula = Formula(formula_dict['name'],
                              formula_dict['id']    )
        return new_formula

    def create_formula(self, formula_dict):  # 通过输入，来生产公式实例
        return
