#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'material mould. '

__author__ = 'ZHU Guilong'


from solution import Point

# 通过字典初始化站点
resource_items = [{
    "类型":     0,
    "名称":     "铝合金",
    "数量":     20
}, {
    "类型":     0,
    "名称":     "废液",
    "数量":     1
}]


# 通用模块
str_multi_channel = {
    "name":         "多通道连接模块",
    "id":           1,

    "sockets_num":  4,
    "plug_num":     4,

    "vessel":       "核心编号"
}

# 1进n出模块，拆分
str_multi_channel = {
    "name":         "多通道连接模块",
    "id":           1,
    "sockets_num":  1,
    "plug_num":     5,
    "vessel":       "传送"
}

# n进1出模块，合并
str_multi_channel = {
    "name":         "多通道连接模块",
    "id":           1,

    "sockets_num":  5,
    "plug_num":     1,

    "vessel":       "传送"
}

# 1进1出模块，传送带
str_multi_channel = {
    "name":         "多通道连接模块",
    "id":           1,

    "sockets_num":  5,
    "plug_num":     1,

    "vessel":       "传送"
}


# 仓库
str_multi_channel = {
    "name":         "Warehouse",
    "id":           1,

    "sockets_num":  3,
    "plug_num":     3,

    "vessel":       "储存"
}

# 金库，需要消耗资金，资金的消耗需要接入金库；
str_multi_channel = {
    "name":         "vault",
    "id":           1,

    "sockets_num":  3,
    "plug_num":     3,

    "vessel":       "储存"
}
