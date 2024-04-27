#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# solution_layer
# 基础求解代码

'layout mould. Create a map. '

__author__ = 'ZHU Guilong'

import sys
import time
import copy
from abc import ABCMeta, abstractmethod
from enum import Enum

from definition import Definition
import material
import formula
from constant import TIME_UNIT
from constant import FLOW_RATE

from position import Position  # 默认最大流速 50 pcs

'''
主要功能：
1. 从配置文件，生产站点；
2. 定义组合站点；
'''


class Route(metaclass=ABCMeta):

    @abstractmethod
    def refresh(self):
        pass




class Frame(Element):
    ''' 
    基础框架
    1. 集合内, 包括elements;
    2. 最小的开关启动单位；
    '''

    def __init__(self):
        self.__aera = '20x30'  # 区域面积




def main():

    # 创建4个节点
    print("开始画点")
    A = Point("A", 5, 5)  # 新建一个具有4进4出的节点，名称为A
    B = Point("B", 5, 5)
    C = Point("C", 5, 5)
    D = Point("D", 5, 5)

    # 创建4条线
    print("开始画线")
    L1 = Line("L1")
    L2 = Line("L2")
    L3 = Line("L3")
    L4 = Line("L4")

    # 分别连接 PlugElement, PlugId, SocketElement, SocketId
    print("开始连接")

    Connection(A.plugs[0], L1.sockets[0])
    Connection(B.plugs[0], L2.sockets[0])
    Connection(L1.plugs[0], C.sockets[0])
    Connection(L2.plugs[0], C.sockets[0])

    Connection(C.plugs[0], L3.sockets[0])
    Connection(L3.plugs[0], A.sockets[0])

    Connection(C.plugs[0], L4.sockets[0])
    Connection(L4.plugs[0], D.sockets[0])

    # -------------------------------------------------------------------------
    # 定义一个站点的反应容器 A

    # self, filter, volume=0, name=None
    p1 = Position(Filter("石油", None), 0, "容器_石油")
    p2 = Position(Filter("铝合金", None), 0, "容器_铝合金")

    V1 = Vessel("机械加工工位")
    V1.insert_position(p1)          # 加入到插槽中
    V1.insert_position(p2)

    A.vessel = V1    # 增加一个容器；

    # -------------------------------------------------------------------------
    # 定义一个站点的反应容器 C

    p3 = Position(Filter("石油", None), 0, "容器_石油")
    p4 = Position(Filter("铝合金", None), 0, "容器_铝合金")

    V2 = Vessel("机械加工工位")
    V2.insert_position(p3)  # 加入到插槽中
    V2.insert_position(p4)

    C.vessel = V2    # 增加一个容器；

    # ----------------------------------
    # 定义一个站点的反应容器 D

    p5 = Position(Filter("石油", None), 0, "容器_石油")
    p6 = Position(Filter("铝合金", None), 0, "容器_铝合金")

    V3 = Vessel("机械加工工位")
    V3.insert_position(p5)  # 加入到插槽中
    V3.insert_position(p6)  # ?

    D.vessel = V3    # 增加一个容器；

    # 汇报
    print("Start...")
    Element.report_all_elements()  # 遍历

    # 遍历
    # 加入一个材料到一个入口；
    # 不停的刷新
    # 不停的汇报

    m1 = material("m1", 50)  # 定义一个材料

    # addObject(A, m1)  # 加入材料，不符合过滤器，则不通过；

    # 启动循环
    i = 0
    while True:
        Element.refresh()
        i += 1
        time.sleep(1)  # 延迟 1 秒
        if i >= 1000:  # 循环1000次后，退出
            break

    print("Finish.")


def translate_between_positions(p1: Position, p2: Position, num: int):
    '''
    在position之间传递物资

    详细描述: 
        从p1向p2传递物资，请求数量为num. 实际传递数量收到p1实际数量、p2剩余容量的影响。

    Args: 
        p1 (Position): 出发点；
        p2 (Position): 目的地；
        num (int): 请求数量。

    Returns: 
        None
    '''

    # case: plug 没有物料
    if p1.real_material == None:
        return

    # case: plug 有物料
    # 计算 p2 实际能接收的物料量
    if p2.real_material == None:  # 没有材料，则有效空间就是容量
        free_space = p2.volume
    else:   # 有材料，则是差值
        free_space = p2.volume - p2.real_material.amount
    # 计算能够传递的材料数量
    real_num = min(free_space, num)

    # case: plug 够
    if p1.real_material.amount >= real_num:  # 够
        if p2.real_material == None:    # p2 没有物料
            p2.real_material = copy.copy(p1.real_material)  # 复制一份；
            p1.real_material.amount -= real_num     # 减去
            p2.real_material.amount = real_num      # 数量赋值
            return

        else:  # 插座有物料
            p1.real_material.amount -= real_num
            p2.real_material.amount += real_num
            return

    else:       # 不够
        if p2.real_material == None:  # 插座没有物料
            p2.real_material = p1.real_material
            p1.real_material = None                 # 直接转移
            return

        else:   # 插座有物料
            p2.real_material.amount += p1.real_material.amount
            del p1.real_material    # 删除插头的；- todo: 不确定是删除，还是？
            return





if __name__ == '__main__':
    main()
