#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-06 Created by tongdg'

from ykb.pc.bill_page import BillPage
import pytest
from tests.ykb.decorator import exception_screenshot

@pytest.mark.smoke
@exception_screenshot()
def test_enter_fill_evecation_bill(multi_browser_driver):
    u"""进入出差申请单-填写出差申请单-断言"""
    driver = multi_browser_driver
    bill_page = BillPage(driver=driver)
    # 普通员工登录
    bill_page.login_ordinary_staff()
    # 切换企业
    bill_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
    bill_page.log.info('--[切换企业ok,登录ok]')

    bill_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    evecation_result = bill_page.enter_fill_evecation_bill()
    assert evecation_result,'进入出差申请单-填写出差申请单-断言失败'

@pytest.mark.smoke
@exception_screenshot()
def test_enter_fill_loan_bill(multi_browser_driver):
    u"""进入借款申请单-填写借款申请单-断言"""
    driver = multi_browser_driver
    bill_page = BillPage(driver=driver)
    # 普通员工登录
    bill_page.login_ordinary_staff()
    # 切换企业
    bill_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
    bill_page.log.info('--[切换企业ok,登录ok]')

    bill_page.log.info('--[进入借款申请单-填写借款申请单-断言]')
    loan_result = bill_page.enter_fill_loan_bill()
    assert loan_result,'进入借款申请单-填写借款申请单-断言失败'

@pytest.mark.smoke
@exception_screenshot()
def test_enter_fill_travel_reimbursement_bill(multi_browser_driver):
    u"""进入差旅报销单-填写差旅报销单-断言"""
    driver = multi_browser_driver
    bill_page = BillPage(driver=driver)
    # 普通员工登录
    bill_page.login_ordinary_staff()
    # 切换企业
    bill_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
    bill_page.log.info('--[切换企业ok,登录ok]')

    bill_page.log.info('--[进入差旅报销单--填写差旅报销单-断言]')
    travel_result = bill_page.enter_fill_travel_reimbursement_bill()
    assert travel_result,'进入差旅报销单--填写差旅报销单-断言失败'

@pytest.mark.smoke
@exception_screenshot()
def test_enter_fill_cost_bill(multi_browser_driver):
    u"""进入费用报销单-填写费用报销单-断言"""
    driver = multi_browser_driver
    bill_page = BillPage(driver=driver)
    # 普通员工登录
    bill_page.login_ordinary_staff()
    # 切换企业
    bill_page.switching_enterprises(_enterprise='tongdg艺赛旗', _login_name='普通员工')
    bill_page.log.info('--[切换企业ok,登录ok]')

    bill_page.log.info('--[进入费用报销单-填写费用报销单-断言]')
    cost_result = bill_page.enter_fill_cost_bill()
    assert cost_result,'进入费用报销单-填写费用报销单-断言失败'

