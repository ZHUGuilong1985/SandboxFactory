#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. 定义具体的材料、设备、人员等等，相当于Excel表格。'

__author__ = 'ZHU Guilong'

from constant import TIME_UNIT


class MaterialPosition:
    def __init__(self, tp, material_name, num):

        self.material_name = material_name

        # self.filter = filter  # 过滤器，实际上就是材料名称；
        self.num = num
        self.type_material = tp  # in, out, hold, other
        # self.speed = 20 #


class Formula():
    ''' 
    典型配方：
    1. 硬件: 
        machine1,   需要电
        worker1,    需要现金；
    1. 输入: 
        inner1，
        inner2，
    2. 输出: 
        outter1, 
        outter2, 
    3. 过程

    (in station2): 材料1 x20 + 材料2 x 12 -(5min x 12，可暂停)-> 产品1 x2 +废弃物2 x3

    适用于station：
    inner[]
    outter[]
    time
    canPause

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

    def __init__(self,  str_formula):
        # str_formula, dict
        self.formula_name = str_formula["name"]
        self.formula_id = str_formula["id"]
        self.time = str_formula["time"]
        self.canPause = str_formula["canPause"]

        self.material_positions = []        # 容器

        for i in str_formula["items"]:
            self.material_positions = MaterialPosition(
                i["类型"], i["名称"], i["数量"])

    def translation(self):
        pass


class FormulaFactory:

    def new_formula(str_formula: str):  # 通过输入，来生产公式实例
        return Formula(str_formula)
