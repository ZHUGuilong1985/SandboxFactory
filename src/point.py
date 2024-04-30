#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# solution_layer
# 基础求解代码

'layout mould. Create a map. '

__author__ = 'ZHU Guilong'


from abc import ABCMeta, abstractmethod
from enum import Enum


from constant import TIME_UNIT
from constant import FLOW_RATE  # 默认最大流速 50 pcs

from definition import Definition
from interface import Socket, Plug
from solution import Element, Route,    translate_between_positions

from formula import Formula
from vessel import Vessel

default_socket_num = 4
default_plug_num = 4


class Point(Definition, Route):

    def __init__(self, name):
        '''
        it contains sockets, vessel and plugs. 
        between socket and plug, use connection. 
        in sockets, vessel and plugs, have positions. 
        '''
        self.name = name  # 名称

        # 默认设置参数
        self.socket_num = default_socket_num
        self.plug_num = default_plug_num

        # 公式
        self.formula = None

        # 对象
        self.sockets  = []  # : Socket
        self.vessel : Vessel = None    # 容器
        self.plugs    = []

        self.init_objects()

        self.report()

    def init_objects(self):
        for i in range(1, self.socket_num):
            self.sockets.append(Socket(self, i))
        for i in range(1, self.plug_num):
            self.plugs.append(Plug(self, i))
        pass

    def setup_by_formula(self, formu: Formula):
        # 根据公式进行设置
        

        pass

    def draw(self):
        # 画本体
        pass

    def __str__(self):
        return self.name

    def report(self):
        print(f"Point {self.name} created. ")
        return

    def fill_sockets(self):
        '''
        插孔
        psts1 -> psts2
        不同的是，一一对应；
        1. socket, 按socket填充；1对1的填充，按照匹配来；
        内部流速，无限大
        '''

        for i in self.sockets:
            if i.match_interface != None:  # 已匹配
                translate_between_positions(
                    i.match_interface.position, i.position, FLOW_RATE)

    def fill_vessel(self):
        # psts1 -> psts2
        # 填充容器，主要功能：
        # 1. 按照公式，填充容器；
        # 2. vessel, 按照pst的in填充；1对多的填充

        for i in self.vessel.positions:
            if i.pst_tp == "in":
                # 从插头处获取材料
                for j in self.sockets:  # point 的 sockets
                    translate_between_positions(j.position, i, FLOW_RATE)

    def fill_plugs(self):
        '''
        插头
        3. plug, 按plug填充； 多对1的填充；可以多个出口出材料
        todo, 需要解决堆积的问题；
        '''
        for i in self.plugs:     # 出口
            for j in self.vessel.positions:    # 反应器
                if j.pst_tp == "out":
                    translate_between_positions(j, i.position, FLOW_RATE)

    def refresh_pre(self):
        '''
        预处理preproccess
        '''
        self.fill_sockets(self.sockets)  # 填充

    def refresh_process(self):
        # 处理
        # 1. 按照坑位设置，自动抓取；
        # 2. 合成

        # 填充
        self.fill_vessel(self.sockets, self.vessel)
        # 反应
        self.vessel.reaction()

    def refresh_post(self):
        '''
        后处理, postprocess
        '''
        self.fill_plugs()  # 填充

    def refresh(self):
        pass
