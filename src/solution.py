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

import material
import formula
from constant import TIME_UNIT
from constant import FLOW_RATE  # 默认最大流速 50 pcs

'''
主要功能：
1. 从配置文件，生产站点；
2. 定义组合站点；
'''


class Route(metaclass=ABCMeta):

    @abstractmethod
    def refresh(self):
        pass


class Element(metaclass=ABCMeta):
    '''
    基础类；
    实现的功能：
    1. 统计所有元素的数量
    2. 共性功能，比如报告
    3. 遍历所有元素
    最小独立单元；
    '''

    element_list = []  # 所有元素列表

    def __init__(self, name):
        self.__name = name  # 名称

    @abstractmethod
    def draw(self):
        '''        
        实现绘画
        '''
        pass

    def __str__(self):
        return self.__name

    def report(self):
        pass

    def report_all_elements():
        for i in Element.element_list:
            i.report()

    def refresh():
        # 由于曾在嵌套，需要优化更新顺序！内部的需要提前优化；
        # todo

        # 预处理
        for i in Element.element_list:
            i.refresh_pre()

        # 处理
        for i in Element.element_list:
            i.refresh_process()

        # 后处理
        for i in Element.element_list:
            i.refresh_post()

    def linkCheck():
        # 检查接口是否正常
        return True


class Filter:
    '''
    过滤器
    '''

    def __init__(self, material_name:   str, parent=None):
        # 按名字过滤，当前是单一过滤器
        self.material_name = material_name
        self.parent = parent            # 安装位置

    def check(self, obj_name):
        if obj_name == self.material_name:
            return True
        else:
            return False

    def __eq__(self, __value) -> bool:
        '''
        只要过滤装置名称相同，就返回True
        '''
        if self.material_name == __value.material_name:
            return True
        else:
            return False


class Position:
    '''
    一个过滤器、一个容器
    position之间的物资传递，作为重点动作考虑；
    '''

    def __init__(self, filter, volume=0, name=None, pst_tp="other"):
        self.name = name
        self.real_material = None   # 所装材料
        # self.quantity = 0
        self.volume = volume        # 容量. 0 代表不限量
        self.filter = filter        # 按照名字过滤
        self.pst_tp = pst_tp          # in,out,hold,other

    def isEmpty(self):
        if self.real_material == None:
            return True
        else:
            return False


class Vessel:
    '''
    point的反应容器，相当于公式；可以接收公式；
    几种反应容器：
    1. 加工厂；
    2. 连接器、传送带
    3. 仓库；
    4. 发生器；
    5. 处理厂；
    '''

    def __init__(self,
                 name=None,
                 formula=None):

        self.name = name

        self.positions = []         # 容器
        self.timer = 0              # 计时器, min
        self.is_processing = False   # 是否在反应中，反应中，输入、输出均锁定；

        self.formula = formula          # 公式

        self.set_positions(formula)     # 设置容器

    def check_condition(self):
        # in端：
        # hold端
        # out端，为空。如果不为空，会造成堵塞；
        # 按照公式检查：

        for i in self.formula.material_positions:

            if i.type_material == "in":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount < i.num:  # 不足
                            return False

            elif i.type_material == "out":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount > 0:  # 滞留
                            return False

            elif i.type_material == "hold":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount < i.num:  # 不足
                            return False

            else:   # other
                continue

        return True

    def reaction(self):
        '''
        检查容器位子，
        符合条件，
            就开始计时，
            时间到后，
            就删除原来的物料，
            再添加新的物料
        '''
        if not self.is_processing:           # 没有在反应中
            if self.check_condition():      # 符合反应条件，启动反应
                self.timer = 0              # 重置计时器
                self.timer += TIME_UNIT     # 加上一个时间周期
                self.is_processing = True    # 锁定进程
                return
            else:   # 不符合反应条件
                return

        else:  # 在反应中
            self.timer += TIME_UNIT  # 加上一个时间周期

            if self.timer >= self.formula.time:  # 到达、超过反应时间
                for i in self.positions:
                    if i.pst_tp == "in":
                        i.real_material.amount = 0
                    elif i.pst_tp == "out":
                        i.real_material.amount = i.volume  # 等于设置产出；
                    elif i.pst_tp == "hold":
                        pass
                    else:  # other
                        pass
                # 重置参数
                self.timer = 0
                self.is_processing = False
            else:
                pass

    def insert_position(self, position):
        '''
        增加空位
        '''
        self.positions.append(position)

    def set_positions(self, formula):
        self.positions.clear()  # 清空
        for i in formula.material_positions:
            self.positions.append(
                Position(i.type_material,  i.num, i.type_material + "_位", i.type_material))


class Connection:
    '''
    定义连接
    '''

    def __init__(self, plug, socket):  # 创建连接
        self.plug = plug
        self.socket = socket

        # 两边记录匹配
        self.plug.connection = self  # return the connection.
        self.plug.match_interface = self.socket

        self.socket.connection = self   # return the connection.
        self.socket.match_interface = self.plug

        print("{}和{}建立连接".format(self.plug.parent.name, self.socket.parent.name))

    def disconnect(self):
        del self

    def __delete__(self):  # 删除时，解除两边
        self.plug.connection = None
        self.plug.match_interface = None
        self.socket.connection = None
        self.socket.match_interface = None

        print("{}和{}断开连接".format(self.plug.parent.name, self.socket.parent.name))

    def transport(self, num):
        '''
        transport objects from plug to socket. 
        本质上是position之间的物资传递？
        '''

        # 没有位置，退出
        if self.plug.position == None or self.socket.position == None:
            return

        # case: plug 没有物料
        if self.plug.position.real_material == None:
            return

        # case: plug 有物料
        # 计算 socket 实际能接收的物料量

        if self.socket.position.real_material == None:  # 没有材料，则有效空间就是容量
            free_space = self.socket.position.volume

        else:   # 有材料，则是差值
            free_space = self.socket.position.volume - \
                self.socket.position.real_material.amount

        # 计算能够传递的材料数量
        if free_space >= num:
            real_num = num
        else:
            real_num = free_space

        # case: plug 够
        if self.plug.position.real_material.amount >= real_num:  # 够
            if self.socket.position.real_material == None:  # 插座没有物料
                m = self.plug.position.real_material     # 材料
                m2 = copy.copy(m)               # 复制一份；
                m.amount -= real_num    # 减去
                m2.amount = real_num    # 数量赋值
                self.socket.position.real_material = m2
                return

            else:  # 插座有物料
                self.plug.position.real_material -= real_num
                self.socket.position.real_material -= real_num
                return

        else:       # 不够
            if self.socket.position.real_material == None:  # 插座没有物料
                self.socket.position.real_material = self.plug.position.real_material
                self.plug.position.real_material = None  # 直接转移
                return

            else:   # 插座有物料
                self.socket.position.real_material += self.plug.position.real_material
                del self.plug.position.real_material    # 删除插头的；
                return


class Interface:
    pass


class Plug(Interface):
    '''
    插头, plug
    '''

    def __init__(self, parent, id, name=None):
        self.__name = name

        self.parent = parent  # 插槽
        self.id = id          # 接口编号，实际上就是数组的编号；通过parent和id可以连接到接口

        # self.filters = None     # 过滤器

        self.match_interface = None  # 为空，代表为未连接
        self.connection = None      # 为空，代表为未连接

        self.position = None        # 容器, 装载设备、人员、材料、半成品等等；
        self.calculator = None      # 计算器，实现物料的流动；每一个节点流动，实现整体的流动；


class Socket(Interface):
    '''
    插座, socket
    '''

    def __init__(self, parent, id, name=None):

        self.__name = name

        self.parent = parent  # 插槽
        self.id = id          # 接口编号，实际上就是数组的编号；通过parent和id可以连接到接口

        # self.filters = None # 过滤器

        self.match_interface = None     # 为空，代表为未连接
        self.connection = None          # 为空，代表为未连接

        self.position = None        # 容器, 装载设备、人员、材料、半成品等等；
        self.calculator = None      # 计算器，实现物料的流动；每一个节点流动，实现整体的流动；


class Point(Element, Route):

    def __init__(self, name):
        '''
        it contains sockets, vessel and plugs. 
        between socket and plug, use connection. 
        in sockets, vessel and plugs, have positions. 
        '''
        self.name = name  # 名称

        socket_num = 4
        plug_num = 4

        self.sockets = []
        for i in range(1, socket_num):
            self.sockets.append(Socket(self, i))

        self.plugs = []
        for i in range(1, plug_num):
            self.plugs.append(Plug(self, i))

        self.vessel = None                  # 容器

        Element.element_list.append(self)   # 登记到类列表

        # 计算器，实现物料的流动；每一个节点流动，实现整体的流动；
        self.calculator = None

        self.report()

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

    def new_by_text(self, text):
        pass


class PointFactory():
    # 生成器

    def __init__(self):
        pass

    def new_point(self, name):
        # 从配置文件生产point

        pass


class Frame(Element):
    ''' 
    基础框架
    1. 集合内, 包括elements;
    2. 最小的开关启动单位；
    '''

    def __init__(self):
        self.__aera = '20x30'  # 区域面积


class FrameFortory():
    pass


class Line(Element):
    ''' 
    线. 特殊的点，只包含：一个插座、一个插头、一个容器。容器不具公式，只是传递。
    '''

    def __init__(self, name=None):
        '''
        创建连接，并连接到两个对象
        '''
        self.name = name

        self.sockets = []
        self.sockets.append(Socket(self, 0))    # socket
        self.plugs = []
        self.plugs.append(Plug(self, 0))        # plug，插头

        self.vessel = Vessel("-", "-")           # 容器

        Element.element_list.append(self)

        self.report()

    def draw(self):
        pass

    def __str__(self):
        return self.name

    def report(self):
        print(f"Line {self.name} created. ")

    def refresh():
        pass

    def refresh_pre(self):
        pass

    def refresh_process(self):
        pass

    def refresh_post(self):
        pass


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


class BaseBiulder():
    def __init__(self) -> None:
        pass

    def build(self, dict=None):
        pass


if __name__ == '__main__':
    main()
