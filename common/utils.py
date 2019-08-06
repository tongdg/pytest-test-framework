#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-30 Created by tongdg'

import time

class Utils:
    """
        常用公用方法
    """
    # 生成报告的名字格式
    @property
    def generate_time(self):
        return str(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))

    # 获取年月日的格式为XXXX(年)-XX(月)-XX(日)
    @property
    def get_year_month_day(self):
        local_time = time.localtime()
        year = str(local_time.tm_year)
        month = local_time.tm_mon
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = local_time.tm_mday
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        local_time = year + '-' + month + '-' + day
        return local_time

    # 获取当前day
    @property
    def get_day(self):
        local_time = time.localtime()
        day = local_time.tm_mday
        return day



    # 获取年月日的格式为XX(时)-XX(分)-XX(秒)
    @property
    def get_hour_min_sec(self):
        local_time = time.localtime()
        hour = local_time.tm_hour
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        min = local_time.tm_min
        if min < 10:
            min = '0' + str(min)
        else:
            min = str(min)
        sec = local_time.tm_sec
        if sec < 10:
            sec = '0' + str(sec)
        else:
            sec = str(sec)
        local_time = hour + '-' + min + '-' + sec
        return local_time




