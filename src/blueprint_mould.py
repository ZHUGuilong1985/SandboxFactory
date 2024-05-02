#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'blueprint data. '

__author__ = 'ZHU Guilong'

from enum import Enum
from constant import TIME_UNIT

# 通过字典初始化站点
elements_list = [
    {
        "point_name":     "净化车间",
        "point_id":     1
    }, {
        "point_name":     "热压罐",
        "point_id":     2
    }, {
        "point_name":     "五轴CNC",
        "point_id":     3
    }, {
        "point_name": "打磨间",
        "point_id":     4
    }, {
        "point_name": "传送带1",
        "point_id":     5
    }, {
        "point_name":     "传送带2",
        "point_id":     6
    }]


links_list = [
    {
        "IN_ID":        1,  # 链接对象
        "PLUG_ID":      25,  # 插头编号
        "OUT_ID":       2,  # 链接对象
        "SOCKET_ID":    51  # 插座编号
    }, {
        "IN_ID":        1,
        "PLUG_ID":      25,
        "OUT_ID":       2,
        "SOCKET_ID":    51
    }]

inputs_list = [{
    "socket_id":    1,
    "point_name":     "净化车间",  # 链接到内部point的socket
    "point_id":     1,
    "IN_ID":        1,
    "PLUG_ID":      21,
}, {
    "socket_id":    2,
    "point_name":     "净化车间",
    "point_id":     1,
    "IN_ID":        1,
    "PLUG_ID":      22
}]


outputs_list = [{
    "plug_id":      1,    # 编号
    "point_name":     "打磨间",     # 链接到内部point的plug
    "point_id":     4,
    "IN_ID":        1,
    "PLUG_ID":      22,
    "output_material":   "产品"
}, {
    "plug_id":      2,  # 编号
    "point_name":     "打磨间",
    "point_id":     4,
    "IN_ID":        1,
    "PLUG_ID":      22,
    "output_material":   "产品"
}]


str_multi_channel = {
    "name":             "典型复材车间",
    "sbid":               1,

    "elements_list":    [],     # 元素清单
    "links_list":       [],     # 连接清单

    # 对于frame，
    "inputs_list":      [],     # 输入接口
    "outputs_list":     []     # 输出接口

}
