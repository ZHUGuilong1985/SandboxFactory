#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. 定义具体的材料、设备、人员等等，相当于Excel表格。'

__author__ = 'ZHU Guilong'

from constant import TIME_UNIT
from enum import Enum

from definition import Definition

# class LogicType(Enum):
#     NEW = 1             # 发生器 +
#     MANUFACTURE = 2     # 制造
#     RECYCLE = 3         # 回收 -
#     TRANSPORT = 4       # 传送 ->
#     STORAGE = 5         # 存储 =
#     CHANNEL = 6         # 多通道


class MaterialPosition:

    def __init__(self, tp, material_name, num):

        self.material_name = material_name

        # self.filter = filter  # 过滤器，实际上就是材料名称；
        self.num = num
        self.type_material = tp  # in, out, hold, other
        # self.speed = 20


class Formula(Definition):
    '''
    formula:
    position_id: [null,0,1,2...]
    match_table: [2,90,100%]
    '''

    def __init__(self, root, sbid=None, name=None, description=None):
        super().__init__(root, sbid)

        self.name = name

        self.support = []
        self.input = []
        self.output = []
        self.matching_table = []  # 匹配表，传送装置才会有。
        self.time = 0
        self.can_pause = True

        self.desription = ''

    def add_list(self, dict, lst):
        # { 'sbid': 'xxxx-xxxx-xxxx-xxxx', 'qty': 1 }
        obj = self.root_container.get_object_by_sbid(dict['sbid'])
        if obj:
            lst.append(
                {"obj":             obj,
                 "qty":             dict['qty'],
                 "_description":    dict['_description'],
                 "position":        dict['position']})
            return True
        else:
            return False

    def add_matching_table(self, dict):
        '''
        {
            'in': 1,
            'out': 2,
            'percent': 0.900
        }
        '''
        self.matching_table.append(dict)

    def set_input(self, lst):
        self.input.clear()
        for item in lst:
            self.add_list(item, self.input)

    def set_output(self, lst):
        self.output.clear()
        for item in lst:
            self.add_list(item, self.output)

    def set_support(self, lst):
        self.support.clear()
        for item in lst:
            self.add_list(item, self.support)

    def set_matching_table(self, lst):
        self.matching_table.clear()
        for item in lst:
            self.add_matching_table(item)

    def set_data(self, dict):
        pass


class FormulaFactory:
    def __init__(self, root):
        self.root = root

    def load_formula(self, dict):  # 通过输入，来生产公式实例

        new_formula = Formula(dict['sbid'], dict['name'])

        # 设置信息
        new_formula.set_support(dict['support'])
        new_formula.set_input(dict['inputs'])
        new_formula.set_output(dict['outputs'])
        new_formula.set_matching_table(dict['matching_table'])

        new_formula.set_time(dict['time'])
        new_formula.set_can_pause(dict['can_pause'])

        return new_formula

    def create_formula(self, formula_dict):  # 通过输入，来生产公式实例
        return
