#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from ykb.pc.approval_page import ApprovalPage
import pytest
from tests.ykb.decorator import exception_screenshot

@pytest.mark.parametrize(
    'enterprise,login_name,department,project',
    [('tongdg艺赛旗','普通员工','ykb-测试小组','ykb-测试项目')]
)
@exception_screenshot()
def test_evection_process1(multi_browser_driver,enterprise,login_name,department,project):
    u"""出差申请单-两个会签-业务（过滤）-直属领导"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    result = appro_page.enter_fill_evecation_bill(department,project)
    assert result, '进入出差申请单-填写出差申请单-断言失败'

    appro_page.log.info('--[项目经理登录]')
    appro_page.login_project_manager()

    appro_page.log.info('--[项目经理查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result,'项目经理查找单据失败'

    appro_page.log.info('--[项目经理会签状态-断言]')
    result = appro_page.judge_approval_process('会签中')
    assert result,'项目经理会签状态断言失败'

    appro_page.log.info('--[项目经理会签同意-断言]')
    result = appro_page.approval_old_agree(['部门领导'])
    assert result,'下一个环节审批领导断言失败'

    appro_page.log.info('--[项目经理会签确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result,'项目经理会签审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('会签中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree(['部门领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

    # 部门领导审批
    appro_page.log.info('--[部门领导登录]')
    appro_page.login_department_leader()

    appro_page.log.info('--[部门领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '部门领导查找单据断言失败'

    appro_page.log.info('--[部门领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '部门领导审批状态断言失败'

    appro_page.log.info('--[部门领导业务同意-断言]')
    result = appro_page.approval_old_agree(['公司领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[部门领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree([''])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

@pytest.mark.parametrize(
    'enterprise,login_name',
    [('tongdg艺赛旗','普通员工')]
)
@exception_screenshot()
def test_evection_process2(multi_browser_driver,enterprise,login_name):
    u"""出差申请单-业务-直属领导"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    result = appro_page.enter_fill_evecation_bill()
    assert result, '进入出差申请单-填写出差申请单-断言失败'

    appro_page.log.info('--[部门领导登录]')
    appro_page.login_department_leader()

    appro_page.log.info('--[部门领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '部门领导查找单据断言失败'

    appro_page.log.info('--[部门领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '部门领导审批状态断言失败'

    appro_page.log.info('--[部门领导业务同意-断言]')
    result = appro_page.approval_old_agree(['公司领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[部门领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree([''])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

@pytest.mark.parametrize(
    'enterprise,login_name,department',
    [('tongdg艺赛旗','普通员工','ykb-测试小组')]
)
def test_evection_process3(multi_browser_driver,enterprise,login_name,department):
    u"""出差申请单-部门带出会签-业务（过滤）-直属领导"""

    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    result = appro_page.enter_fill_evecation_bill(department=department)
    assert result, '进入出差申请单-填写出差申请单-断言失败'

    # 会签带出来 1人会签转业务
    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree(['部门领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

    appro_page.log.info('--[部门领导登录]')
    appro_page.login_department_leader()

    appro_page.log.info('--[部门领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '部门领导查找单据断言失败'

    appro_page.log.info('--[部门领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '部门领导审批状态断言失败'

    appro_page.log.info('--[部门领导业务同意-断言]')
    result = appro_page.approval_old_agree(['公司领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[部门领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree([''])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

@pytest.mark.parametrize(
    'enterprise,login_name,project',
    [('tongdg艺赛旗','普通员工','ykb-测试项目')]
)
@exception_screenshot()
def test_evection_process4(multi_browser_driver,enterprise,login_name,project):
    u"""出差申请单-项目带出会签-业务-直属领导"""

    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    evecation_result = appro_page.enter_fill_evecation_bill(project=project)
    assert evecation_result, '进入出差申请单-填写出差申请单-断言失败'

    # 会签带出来 1人会签转业务
    appro_page.log.info('--[项目经理登录]')
    appro_page.login_project_manager()

    appro_page.log.info('--[项目经理查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '项目经理查找单据失败'

    appro_page.log.info('--[项目经理会签状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '项目经理会签状态断言失败'

    appro_page.log.info('--[项目经理会签同意-断言]')
    result = appro_page.approval_old_agree(['部门领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[项目经理会签确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '项目经理会签审批失败'

    appro_page.log.info('--[部门领导登录]')
    appro_page.login_department_leader()

    appro_page.log.info('--[部门领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '部门领导查找单据断言失败'

    appro_page.log.info('--[部门领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '部门领导审批状态断言失败'

    appro_page.log.info('--[部门领导业务同意-断言]')
    result = appro_page.approval_old_agree(['公司领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[部门领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree([''])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'

@pytest.mark.parametrize(
    'enterprise,login_name',
    [('tongdg艺赛旗','普通员工')]
)
@exception_screenshot()
def test_evection_process5(multi_browser_driver,enterprise,login_name):
    u"""出差申请单(填写机票，酒店)-业务-直属领导"""

    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[进入出差申请单-填写出差申请单-断言]')
    result = appro_page.enter_fill_evecation_bill(switch=True)
    assert result, '进入出差申请单-填写出差申请单-断言失败'

    appro_page.log.info('--[部门领导登录]')
    appro_page.login_department_leader()

    appro_page.log.info('--[部门领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '部门领导查找单据断言失败'

    appro_page.log.info('--[部门领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '部门领导审批状态断言失败'

    appro_page.log.info('--[部门领导业务同意-断言]')
    result = appro_page.approval_old_agree(['公司领导'])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[部门领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[公司领导登录]')
    appro_page.login_company_leader()

    appro_page.log.info('--[公司领导查找单据-断言]')
    result = appro_page.enter_list_find_old_bill()
    assert result, '公司领导查找单据断言失败'

    appro_page.log.info('--[公司领导审批状态-断言]')
    result = appro_page.judge_approval_process('审批中')
    assert result, '公司领导审批状态断言失败'

    appro_page.log.info('--[公司领导业务同意-断言]')
    result = appro_page.approval_old_agree([''])
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[公司领导业务确定-断言]')
    result = appro_page.old_apply_confirm()
    assert result, '公司领导业务审批失败'


