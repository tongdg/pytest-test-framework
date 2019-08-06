#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2018-06-04 Created by tongdg'
import os

"""
path配置
"""
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
REPORT_PATH = os.path.abspath(os.path.join(BASE_PATH,"report"))

"""
测试数据配置
"""
# JC切换企业测试数据配置

def get_enterprise_login():
    data = []
    # JC切换企业测试数据配置
    # 企业名称 用户名 都正确
    data.append(['测试一下下','童定国'])
    # 企业名称正确 用户名不正确
    data.append(['测试一下下','tdg'])
    # 企业名称不正确 用户名不正确
    data.append(['测试一下','tdg'])
    # 企业名称不正确 用户名正确
    data.append(['测试一下', '童定国'])

    # # ZS
    # # 企业名称 用户名 都正确
    # data.append(['云快报上海', '童定国'])
    # # 企业名称正确 用户名不正确
    # data.append(['云快报上海', 'tdg'])
    # # 企业名称不正确 用户名不正确
    # data.append(['云快报上海嗨嗨', 'tdg'])
    # # 企业名称不正确 用户名正确
    # data.append(['云快报上海嗨嗨', '童定国'])
    return data

# ZS切换企业测试数据配置

# 测试地址
# 集成测试地址
INTEGRATE_ADDRESS = 'http://120.132.23.147:840/logon'
# 正式测试地址
FORM_ADDRESS = 'https://www.51ykb.com/Logon'
# 获取测试地址
def get_test_address():
    return INTEGRATE_ADDRESS

# 移动测试地址
MOBILE_INTEGRATE_ADDRESS = 'http://test.m.51ykb.com/Public/index.html?#/login'
# 获取移动测试地址
def get_mobile_test_address():
    return MOBILE_INTEGRATE_ADDRESS


















