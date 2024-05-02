#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'material mould. '

__author__ = 'ZHU Guilong'

from enum import Enum

from constant import TIME_UNIT


class ItemsType(Enum):
    IN = 1
    HOLD = 2
    OUT = 3


class LogicType(Enum):
    NEW = 1             # 发生器 +
    MANUFACTURE = 2     # 制造
    RECYCLE = 3         # 回收 -
    TRANSPORT = 4       # 传送 ->
    STORAGE = 5         # 存储 =
    CHANNEL = 6         # 多通道


# 系统默认公式

# 这个变量用于formula的初始化，生产类的实例；
# 后续也要通过一个程序，来生产这个变量；
resource_items = [{
    "类型":     ItemsType.IN,
    "名称":     "铝合金",
    "数量":     20
}, {
    "类型":     ItemsType.IN,
    "名称":     "切削液",
    "数量":     50
}, {
    "类型":     ItemsType.HOLD,
    "名称":     "机床",
    "数量":     1
}, {
    "类型":     ItemsType.HOLD,
    "名称":     "操作工",
    "数量":     1
}, {
    "类型":     ItemsType.OUT,
    "名称":     "产品A",
    "数量":     1
}, {
    "类型":     ItemsType.OUT,
    "名称":     "废液",
    "数量":     1
}]

str_formula = {
    "name":         "产品A加工",
    "sbid":           1,
    "items":        resource_items,   # 公式主体
    "time":         120,
    "can_pause":     True,
    "logic":        LogicType.MANUFACTURE
}

# 写一个万能传送带的公式，流量在进出口控制
'''
规律总结为：
1. 有一个流量限制，比如50/单位时间；
2. 低于这个流量，直接传递；
3. 高于这个流量的，只能通过50/单位时间；
4. 如果前方堵塞，则只能通过out口剩余的数量；
5. 不具备储存功能，最大量即为out一个单位周期的数量和plug口的流量，
6. plug的流量为固定值，

逻辑：
1. out不足的情况下，有多少从in补多少；
1. 只检查入口数量不大于50；
'''

# 根据反应规则，不到这个数量，不会反应；
#  0，表示来多少反应多少；
# -1，表示不受数量上限影响；如何设置存储空间；
resource_items = [{
    "类型":     ItemsType.IN,
    "名称":     None,
    "数量":     0
}, {
    "类型":     ItemsType.OUT,
    "名称":     None,
    "数量":     999999
}]

str_formula = {
    "name":         "传送带",
    "sbid":           2,
    "items":        resource_items,
    "time":         TIME_UNIT,
    "can_pause":     True,
    "logic":        LogicType.TRANSPORT
}

# 写一个发生器, 单位时间生产 20 个预浸料
resource_items = [{
    "类型":     ItemsType.IN,
    "名称":     None,
    "数量":     0
}, {
    "类型":     ItemsType.OUT,
    "名称":     "预浸料",
    "数量":     20
}]

str_formula = {
    "name":         "发生器",
    "sbid":           3,
    "items":        resource_items,
    "time":         TIME_UNIT,
    "can_pause":     True,
    "logic":        LogicType.NEW
}


# 写一个回收器，消失，释放内存；
# 不区分类，只要东西来就消失。可以通过过滤器来设置开关；

resource_items = [{
    "类型":     ItemsType.IN,
    "名称":     None,
    "数量":     0
}, {
    "类型":     ItemsType.OUT,
    "名称":     None,
    "数量":     0
}]

str_formula = {
    "name":         "回收器",
    "sbid":           4,
    "items":        resource_items,
    "time":         TIME_UNIT,
    "can_pause":     True,
    "logic":        LogicType.RECYCLE
}


# 写一个库房，不加过滤器，就要能存放任何东西
# out, 设多个栏位，放物品；
# in，不管，只做传递；甚至直接到out

resource_items = [{
    "类型":     ItemsType.IN,
    "名称":     None,
    "数量":     0
}, {
    "类型":     ItemsType.OUT,
    "名称":     None,
    "数量":     0
}]

str_formula = {
    "name":         "库房",
    "sbid":           5,
    "items":        resource_items,
    "time":         TIME_UNIT,
    "can_pause":     True,
    "logic":        LogicType.STORAGE
}
