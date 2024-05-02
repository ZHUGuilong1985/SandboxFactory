#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'日历模块'

__author__ = 'ZHU Guilong'

from enum import Enum

import datetime

'''
配置日历
计算加班、薪水

'''

pay_day = 10  # 发薪日

Multiplier_for_overtime_pay = 2  # 加班工资倍数


class ItemsType(Enum):
    # 上班制度

    classes_08 = 1          # 8小时工作
    classes_12_12 = 2       # 两班倒
    classes_08_08_08 = 3    # 三班倒

    classes_08_x4 = 4       # 8小时工作，按需求需要加班，不超过12小时


class WorkBy(Enum):
    work_by_week = 1
    work_by_month = 0


iswork_normal = {
    "Monday":       1,
    "Tuesday":      1,
    "Wednesday":    1,
    "Thursday":     1,
    "Friday":       1,
    "Saturday":     0,
    "Sunday":       0,
}

single_day_weekend = {
    "Monday":       1,
    "Tuesday":      1,
    "Wednesday":    1,
    "Thursday":     1,
    "Friday":       1,
    "Saturday":     1,
    "Sunday":       0,
}


str_days = {
    "sbid":                               1,
    "name":                             "双休员工日历",
    "workby":                           WorkBy.work_by_week,   # 按星期进行；
    "Single_or_double":                 iswork_normal,   # 双休日
    "pay_day":                          pay_day,        # 发薪日
    "Multiplier_for_overtime_pay":      Multiplier_for_overtime_pay  # 倍数
}

str_days = {
    "sbid":                               2,
    "name":                             "单休员工日历",
    "workby":                           WorkBy.work_by_week,   # 按月休息，每个月多少天休息；
    "Single_or_double":                 single_day_weekend,   # 单休日
    "pay_day":                          pay_day,        # 发薪日
    "Multiplier_for_overtime_pay":      Multiplier_for_overtime_pay  # 倍数
}
