#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
CLI的功能：
1. 初始化数据
尽快完成在命令行的运行功能。
'''

from init_default import SetupSystem
import material
import formula
import formula_mould
import solution

from solution import Factory, Workshop, Section, Station
from blueprint import Blueprint
from configuration import Configuration
from sandbox import Sandbox

'main mould. 主要负责程序整体运行；'

__author__ = 'ZHU Guilong'


class Layout:
    '''
    一个完整的定义
    '''

    refresh_cycle = 0  # 刷新周期，用于调试和UI的显示；实际调成0，快速看结果；

    Minimum_computation_period = 5  # 5 min

    def __init__(self):
        '''
        加一个工厂；
        加材料；
        加动力；
        运行；
        统计消耗和产出；

        '''
        pass


class Consume():
    '''
    消耗器，处理材料等损耗

    处理材料流：
    安装在进出口出的损耗配件；
    '''
    pass


class Switch():
    ''' 
    开关模块、阀门
    '''

    def __init__(self) -> None:
        pass


class Timer():
    ''' 
    计时器
    1. 明确计时周期。默认的计算计时周期是5min；一天288个计算周期；
    2. 在此基础上，上班制度
    各个工厂，人员都有自己的计算周期运行一遍；
    如果定义5000个节点，则144万个计算量；
    '''

    def __init__(self) -> None:
        pass


class Update():
    ''' 
    更新模块

    算法实现：
    1. 将所有对象加入到列表中；
    2. 按照更新周期，进行更新；

    更新顺序：
    1. 有两种策略：
        按照加入顺序
        按照生产线顺序；（存在困难，很难梳理出顺序，特别当多出开始时）

    2. 一次更新解决不了问题，可以通过多次叠代；
        但是，多次迭代后需要区域问题；
        最多，达到20叠代后，废弃；

    3. 如何判定结束：
        更新后显示done；
    '''

    def __init__(self) -> None:
        pass

    def report(self):
        ''' 
        报告, 说明自身的基本情况
        '''
        print("update! ")


def create_elements():
    ''' 
    创建常用材料、素材
    1. 用于测试；
    2. 后期，从文件创建；
    '''

    # 设备
    autoclave = material.Machine("autoclave")
    oven = material.Machine("oven")
    CNC_machining_center = material.Machine("CNC_machining_center")

    # 人员
    operator = material.Worker("operator")

    # 材料
    prepreg = material.Material("prepreg")       # 预浸料
    epoxy_resin = material.Material("epoxy_resin")   # 环氧树脂

    # 其他
    compressed_air_800kpa = material.Material("compressed_air_800kpa")   # 压缩空气
    AC220v = material.Material("220v AC")
    AC380v = material.Material("380v AC")
    # 压缩氮气
    compressed_nitrogen = material.Material("compressed_nitrogen")
    # 普通water
    industrial_water = material.Material("industrial_water")
    waste_water = material.Material("waste_water")                       # 污水

    cutter = material.Material("cutter")     # 刀具

    # 新建公式，工艺
    formula_1 = solution.Formula("固化工艺", "")
    formula_2 = solution.Formula("切割工艺", "")

    fty = formula.FormulaFactory()
    formula_1 = fty.new_formula("固化工艺")
    formula_2 = fty.new_formula("切割工艺")

    # 新建配置，工位
    configuration_1 = Configuration("固化工段", "")
    configuration_2 = Configuration("切割工段", "")

    # 新建蓝图，工厂
    blueprint_1 = Blueprint("复合材料工厂", "")


def bulid_factory():
    return Factory()


def check_configeration():
    print("check configuration. ")


def read_configeration():
    print("read configuration. ")
    get_default_resource('.\resouce.json')


def get_default_resource(recource_dict):
    # 读取资源信息
    recource_dict

    print("get default resource. ")
    pass


def start_ui():
    print("start ui. ")


def create_new_factory():
    print("create new factory. ")


def start():
    print('start...')


def main():

    # 加载存在，可以在默认模板下，进行编辑。

    SetupSystem.load_setup('resouce.json')

    #
    sandbox = Sandbox()  # 调试沙盒

    sandbox.load_resource('resouce.json')
    sandbox.run()

    check_configeration()    # 检查文件配置情况
    read_configeration()     # 读取配置文件
    start_ui()               # 启动UI界面，先从命令行接收指令；或者通过读取存档，来初始化工厂
    create_new_factory()    # 新建一个空的工厂
    start()                 # 启动

    create_elements()  # 创建常用材料、素材

    # 定义蓝图：定义工段连接
    blueprint_1 = Blueprint("复合材料工厂", "")

    myfty = Factory(blueprint_1)

    myfty.build()  # 建设工厂
    # myfty.ADD()

    myfty.run()  # 启动


if __name__ == '__main__':
    main()
