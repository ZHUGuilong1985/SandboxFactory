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


class Formula(Definition):
    '''    '''

    def __init__(self, id=None, name=None):
        super().__init__(id)

        self.id = id
        self.name = name

        self.support = []  #
        self.input = []  # 输入
        self.output = []  # 输出
        self.matching_table = []  # 匹配表，传送装置才会有。
        self.time = str_formula["time"]
        self.can_pause = str_formula["canPause"]

        self.desription = '一个公式的描述。'

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

    def set_output(self, lst):
        pass

    def set_support(self, lst):
        # 只添加id，还是需要找到对应的对象？

        self.add_support.clear()  # 清空
        for item in lst: 
            self.add_support(item)

        pass

    def set_matching_table(self, lst):
        pass

    def translation(self):
        pass

def ResourceList():
    def __init__(self):

        self.lst = []

     

class FormulaFactory:

    def load_formula(self, dict):  # 通过输入，来生产公式实例

        new_formula = Formula(dict['id'],dict['name'])

        # 设置信息
        new_formula.set_support(dict['support'])
        new_formula.set_input(dict['inputs'])
        new_formula.set_output(dict['outputs'])
        new_formula.set_time(dict['time'])
        new_formula.set_can_pause(dict['canPause'])


        return new_formula

    '''
    {
        "name": "产品A加工",
        "_description": "在加工中心生产零件。",
        "id": 1,
        "support": [
            {   
                "id":"xxxx-xxxx-xxxx-xxxx",
                "名称": "机床",
                "数量": 1
            },
            {
                "名称": "操作工",
                "数量": 1
            }
        ],
        "inputs": [
            {
                "名称": "铝合金",
                "数量": 20
            },
            {
                "名称": "切削液",
                "数量": 50
            }
        ],
        "outputs": [
            {
                "名称": "产品A",
                "数量": 1
            },
            {
                "名称": "废液",
                "数量": 1
            }
        ],
        "time": 120,
        "can_pause": true,
        "logic": "LogicType.MANUFACTURE"
    }

    '''

    def create_formula(self, formula_dict):  # 通过输入，来生产公式实例
        return
