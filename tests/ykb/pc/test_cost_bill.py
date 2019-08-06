#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-25 Created by tongdg'
from ykb.pc.approval_page import ApprovalPage
import pytest
import allure
from tests.ykb.decorator import exception_screenshot

@pytest.mark.parametrize(
    'enterprise,login_name,project',
    [('tongdg艺赛旗','普通员工','ykb-测试项目')]
)
@exception_screenshot()
def test_cost_bill_process1(multi_browser_driver,enterprise,login_name,project):
    u"""费用报销单-会签（项目）-直属领导（过滤）业务-直属领导-财务-复核-出纳"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
    result = appro_page.enter_fill_cost_bill(project=project)
    assert result, '进入费用报销单-填写费用报销单-断言失败'

    appro_page.log.info('--[ 项目经理登录]')
    result = appro_page.login_project_manager()
    assert result, '项目经理登录失败'

    appro_page.log.info('--[ 项目经理查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '项目经理查找单据失败'

    appro_page.log.info('--[ 项目经理会签状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result,'项目经理会签状态错误'

    appro_page.log.info('--[ 项目经理同意-断言]')
    result = appro_page.approval_new_agree('部门领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 项目经理会签确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '项目经理会签审批失败'

    appro_page.log.info('--[ 部门领导登录]')
    result = appro_page.login_department_leader()
    assert result, '部门领导登录失败'

    appro_page.log.info('--[ 部门领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '部门领导查找单据失败'

    appro_page.log.info('--[ 部门领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '部门领导业务审批状态错误'

    appro_page.log.info('--[ 部门领导同意-断言]')
    result = appro_page.approval_new_agree('公司领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 部门领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[ 公司领导登录]')
    result = appro_page.login_company_leader()
    assert result, '公司领导登录失败'

    appro_page.log.info('--[ 公司领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '公司领导查找单据失败'

    appro_page.log.info('--[ 公司领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '公司领导业务审批状态错误'

    appro_page.log.info('--[ 公司领导同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 公司领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '公司领导业务审批失败'

    appro_page.log.info('--[ 会计登录]')
    result = appro_page.login_accounting()
    assert result, '会计登录失败'

    appro_page.log.info('--[ 会计查找单据-断言]')
    result = appro_page.enter_list_find_finance_reimbursement()
    assert result, '会计查找单据失败'

    appro_page.log.info('--[ 会计审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务初审中')
    assert result, '会计审批状态错误'

    appro_page.log.info('--[ 会计同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 会计审核确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '会计审核失败'

    appro_page.log.info('--[ 财务经理登录]')
    result = appro_page.login_financial_manager()
    assert result, '财务经理登录失败'

    appro_page.log.info('--[ 财务经理查找单据—断言]')
    result = appro_page.enter_list_find_review_reimbursement()
    assert result, '财务经理查找单据失败'

    appro_page.log.info('--[ 财务经理审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务复核中')
    assert result, '财务经理审批状态断言失败'

    appro_page.log.info('--[ 财务经理同意断言]')
    result = appro_page.approval_new_agree()
    assert result, '财务经理同意失败'

    appro_page.log.info('--[ 财务经理审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '财务经理审批确定失败'

    appro_page.log.info('--[ 出纳登录]')
    appro_page.login_cashier()

    appro_page.log.info('--[ 出纳查找单据-断言]')
    result =  appro_page.enter_list_find_payment(bill_type='new')
    assert result,'出纳查找单据断言失败'

    appro_page.log.info('--[ 出纳状态-断言]')
    result = appro_page.judge_new_approval_process('出纳付款中')
    assert result, '出纳状态断言失败'

    appro_page.log.info('--[ 出纳支付-断言]')
    result = appro_page.new_payment()
    assert result, '出纳支付断言失败'


@pytest.mark.parametrize(
    'enterprise,login_name,project',
    [('tongdg艺赛旗','普通员工','ykb-测试项目')]
)
@exception_screenshot()
def test_cost_bill_process2(enterprise,login_name,project,multi_browser_driver):
    u"""费用报销单-会签（项目）-直属领导（过滤）业务-直属领导-财务-加审领导-财务-复核-出纳"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
    result = appro_page.enter_fill_cost_bill(project=project)
    assert result, '进入费用报销单-填写费用报销单-断言失败'

    appro_page.log.info('--[ 项目经理登录]')
    result = appro_page.login_project_manager()
    assert result, '项目经理登录失败'

    appro_page.log.info('--[ 项目经理查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '项目经理查找单据失败'

    appro_page.log.info('--[ 项目经理会签状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '项目经理会签状态错误'

    appro_page.log.info('--[ 项目经理同意-断言]')
    result = appro_page.approval_new_agree('部门领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 项目经理会签确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '项目经理会签审批失败'

    appro_page.log.info('--[ 部门领导登录]')
    result = appro_page.login_department_leader()
    assert result, '部门领导登录失败'

    appro_page.log.info('--[ 部门领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '部门领导查找单据失败'

    appro_page.log.info('--[ 部门领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '部门领导业务审批状态错误'

    appro_page.log.info('--[ 部门领导同意-断言]')
    result = appro_page.approval_new_agree('公司领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 部门领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[ 公司领导登录]')
    result = appro_page.login_company_leader()
    assert result, '公司领导登录失败'

    appro_page.log.info('--[ 公司领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '公司领导查找单据失败'

    appro_page.log.info('--[ 公司领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '公司领导业务审批状态错误'

    appro_page.log.info('--[ 公司领导同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 公司领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '公司领导业务审批失败'

    appro_page.log.info('--[ 会计登录]')
    result = appro_page.login_accounting()
    assert result, '会计登录失败'

    appro_page.log.info('--[ 会计查找单据-断言]')
    result = appro_page.enter_list_find_finance_reimbursement()
    assert result, '会计查找单据失败'

    appro_page.log.info('--[ 会计审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务初审中')
    assert result, '会计审批状态错误'

    appro_page.log.info('--[ 会计加审-断言]')
    result = appro_page.add_approval_finance_confirm()
    assert result, '会计加审失败'

    appro_page.log.info('--[ 加审领导登录]')
    appro_page.login_add_approval()

    appro_page.log.info('--[ 加审领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '加审领导查找单据失败'

    appro_page.log.info('--[ 加审领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务加审中')
    assert result, '加审领导业务审批状态错误'

    appro_page.log.info('--[ 加审领导同意断言]')
    result = appro_page.new_payment()
    assert result, '加审领导同意断言失败'

    appro_page.log.info('--[ 会计登录]')
    result = appro_page.login_accounting()
    assert result, '会计登录失败'

    appro_page.log.info('--[ 会计查找单据-断言]')
    result = appro_page.enter_list_find_finance_reimbursement()
    assert result, '会计查找单据失败'

    appro_page.log.info('--[ 会计审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务初审中')
    assert result, '会计审批状态错误'

    appro_page.log.info('--[ 会计同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 会计审核确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '会计审核失败'

    appro_page.log.info('--[ 财务经理登录]')
    result = appro_page.login_financial_manager()
    assert result, '财务经理登录失败'

    appro_page.log.info('--[ 财务经理查找单据—断言]')
    result = appro_page.enter_list_find_review_reimbursement()
    assert result, '财务经理查找单据失败'

    appro_page.log.info('--[ 财务经理审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务复核中')
    assert result, '财务经理审批状态断言失败'

    appro_page.log.info('--[ 财务经理同意断言]')
    result = appro_page.approval_new_agree()
    assert result, '财务经理同意失败'

    appro_page.log.info('--[ 财务经理审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '财务经理审批确定失败'

    appro_page.log.info('--[ 出纳登录]')
    appro_page.login_cashier()

    appro_page.log.info('--[ 出纳查找单据-断言]')
    result = appro_page.enter_list_find_payment(bill_type='new')
    assert result, '出纳查找单据断言失败'

    appro_page.log.info('--[ 出纳状态-断言]')
    result = appro_page.judge_new_approval_process('出纳付款中')
    assert result, '出纳状态断言失败'

    appro_page.log.info('--[ 出纳支付-断言]')
    result = appro_page.new_payment()
    assert result, '出纳支付断言失败'


@pytest.mark.parametrize(
    'enterprise,login_name',
    [('tongdg艺赛旗','普通员工')]
)
@pytest.mark.smoke
@exception_screenshot()
def test_cost_bill_process3(multi_browser_driver,enterprise,login_name):
    u"""费用报销单-业务-直属领导-财务-加审领导-财务-复核加审-财务总监-出纳"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
    result = appro_page.enter_fill_cost_bill()
    assert result, '进入费用报销单-填写费用报销单-断言失败'

    appro_page.log.info('--[ 部门领导登录]')
    result = appro_page.login_department_leader()
    assert result, '部门领导登录失败'

    appro_page.log.info('--[ 部门领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '部门领导查找单据失败'

    appro_page.log.info('--[ 部门领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '部门领导业务审批状态错误'

    appro_page.log.info('--[ 部门领导同意-断言]')
    result = appro_page.approval_new_agree('公司领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 部门领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[ 公司领导登录]')
    result = appro_page.login_company_leader()
    assert result, '公司领导登录失败'

    appro_page.log.info('--[ 公司领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '公司领导查找单据失败'

    appro_page.log.info('--[ 公司领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '公司领导业务审批状态错误'

    appro_page.log.info('--[ 公司领导同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 公司领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '公司领导业务审批失败'

    appro_page.log.info('--[ 会计登录]')
    result = appro_page.login_accounting()
    assert result, '会计登录失败'

    appro_page.log.info('--[ 会计查找单据-断言]')
    result = appro_page.enter_list_find_finance_reimbursement()
    assert result, '会计查找单据失败'

    appro_page.log.info('--[ 会计审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务初审中')
    assert result, '会计审批状态错误'

    appro_page.log.info('--[ 会计同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 会计审核确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '会计审核失败'

    appro_page.log.info('--[ 财务经理登录]')
    result = appro_page.login_financial_manager()
    assert result, '财务经理登录失败'

    appro_page.log.info('--[ 财务经理查找单据—断言]')
    result = appro_page.enter_list_find_review_reimbursement()
    assert result, '财务经理查找单据失败'

    appro_page.log.info('--[ 财务经理审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务复核中')
    assert result, '财务经理审批状态断言失败'

    appro_page.log.info('--[ 财务经理同意断言]')
    result = appro_page.approval_new_agree()
    assert result, '财务经理同意失败'

    appro_page.log.info('--[ 财务经理添加审批人审批确定-断言]')
    result = appro_page.add_approval_person_review_confirm()
    assert result, '财务经理添加审批人审批确定失败'

    appro_page.log.info('--[ 财务总监登录]')
    appro_page.login_financial_chief_inspector()

    appro_page.log.info('--[ 财务总监查找单据-断言]')
    result = appro_page.enter_list_find_review_reimbursement()
    assert result, '财务总监查找单据断言失败'

    appro_page.log.info('--[ 财务总监审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务总监审核中')
    assert result, '财务总监审批状态断言失败'

    appro_page.log.info('--[ 财务总监同意断言]')
    result = appro_page.approval_new_agree()
    assert result, '财务总监同意失败'

    appro_page.log.info('--[ 财务总监审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '财务总监审批确定失败'

    appro_page.log.info('--[ 出纳登录]')
    appro_page.login_cashier()

    appro_page.log.info('--[ 出纳查找单据-断言]')
    result = appro_page.enter_list_find_payment(bill_type='new')
    assert result, '出纳查找单据断言失败'

    appro_page.log.info('--[ 出纳状态-断言]')
    result = appro_page.judge_new_approval_process('出纳付款中')
    assert result, '出纳状态断言失败'

    appro_page.log.info('--[ 出纳支付-断言]')
    result = appro_page.new_payment()
    assert result, '出纳支付断言失败'

@pytest.mark.parametrize(
    'enterprise,login_name,department,project',
    [('tongdg艺赛旗','普通员工','ykb-测试小组','ykb-测试项目')]
)
@exception_screenshot()
def test_cost_bill_process4(multi_browser_driver,enterprise,login_name,department,project):
    u"""费用报销单-两个会签-直属领导（过滤）业务-直属领导-财务-复核出纳"""
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result, '登录失败！'
    # 切换企业
    result = appro_page.switching_enterprises(_enterprise=enterprise, _login_name=login_name)
    assert result, '企业切换失败！'
    appro_page.log.info('--[切换企业ok,登录ok]')

    appro_page.log.info('--[ 进入费用报销单-填写费用报销单-断言]')
    result = appro_page.enter_fill_cost_bill(department=department,project=project)
    assert result, '进入费用报销单-填写费用报销单-断言失败'

    appro_page.log.info('--[ 项目经理登录]')
    result = appro_page.login_project_manager()
    assert result, '项目经理登录失败'

    appro_page.log.info('--[ 项目经理查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '项目经理查找单据失败'

    appro_page.log.info('--[ 项目经理会签状态-断言]')
    result = appro_page.judge_new_approval_process('会签中','new')
    assert result,'项目经理会签状态错误'

    appro_page.log.info('--[ 项目经理同意-断言]')
    result = appro_page.approval_new_agree('部门领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 项目经理会签确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '项目经理会签审批失败'

    appro_page.log.info('--[ 公司领导登录]')
    result = appro_page.login_company_leader()
    assert result, '公司领导登录失败'

    appro_page.log.info('--[ 公司领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '公司领导查找单据失败'

    appro_page.log.info('--[ 公司领导会签状态-断言]')
    result = appro_page.judge_new_approval_process('会签中','new')
    assert result, '公司领导会签状态错误'

    appro_page.log.info('--[ 公司领导同意-断言]')
    result = appro_page.approval_new_agree('部门领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 公司领导会签确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '公司领导会签审批失败'

    appro_page.log.info('--[ 部门领导登录]')
    result = appro_page.login_department_leader()
    assert result, '部门领导登录失败'

    appro_page.log.info('--[ 部门领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '部门领导查找单据失败'

    appro_page.log.info('--[ 部门领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '部门领导业务审批状态错误'

    appro_page.log.info('--[ 部门领导同意-断言]')
    result = appro_page.approval_new_agree('公司领导')
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 部门领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '部门领导业务审批失败'

    appro_page.log.info('--[ 公司领导登录]')
    result = appro_page.login_company_leader()
    assert result, '公司领导登录失败'

    appro_page.log.info('--[ 公司领导查找单据-断言]')
    result = appro_page.enter_list_find_new_bill()
    assert result, '公司领导查找单据失败'

    appro_page.log.info('--[ 公司领导业务审批状态-断言]')
    result = appro_page.judge_new_approval_process('审批中')
    assert result, '公司领导业务审批状态错误'

    appro_page.log.info('--[ 公司领导同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 公司领导业务审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '公司领导业务审批失败'

    appro_page.log.info('--[ 会计登录]')
    result = appro_page.login_accounting()
    assert result, '会计登录失败'

    appro_page.log.info('--[ 会计查找单据-断言]')
    result = appro_page.enter_list_find_finance_reimbursement()
    assert result, '会计查找单据失败'

    appro_page.log.info('--[ 会计审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务初审中')
    assert result, '会计审批状态错误'

    appro_page.log.info('--[ 会计同意-断言]')
    result = appro_page.approval_new_agree()
    assert result, '下一个环节审批领导断言失败'

    appro_page.log.info('--[ 会计审核确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '会计审核失败'

    appro_page.log.info('--[ 财务经理登录]')
    result = appro_page.login_financial_manager()
    assert result, '财务经理登录失败'

    appro_page.log.info('--[ 财务经理查找单据—断言]')
    result = appro_page.enter_list_find_review_reimbursement()
    assert result, '财务经理查找单据失败'

    appro_page.log.info('--[ 财务经理审批状态-断言]')
    result = appro_page.judge_new_approval_process('财务复核中')
    assert result, '财务经理审批状态断言失败'

    appro_page.log.info('--[ 财务经理同意断言]')
    result = appro_page.approval_new_agree()
    assert result, '财务经理同意失败'

    appro_page.log.info('--[ 财务经理审批确定-断言]')
    result = appro_page.new_bill_confirm_approval()
    assert result, '财务经理审批确定失败'

    appro_page.log.info('--[ 出纳登录]')
    appro_page.login_cashier()

    appro_page.log.info('--[ 出纳查找单据-断言]')
    result = appro_page.enter_list_find_payment(bill_type='new')
    assert result, '出纳查找单据断言失败'

    appro_page.log.info('--[ 出纳状态-断言]')
    result = appro_page.judge_new_approval_process('出纳付款中')
    assert result, '出纳状态断言失败'

    appro_page.log.info('--[ 出纳支付-断言]')
    result = appro_page.new_payment()
    assert result, '出纳支付断言失败'

@allure.feature('test')
@pytest.mark.test
@exception_screenshot()
def test_allure_report(multi_browser_driver):
    driver = multi_browser_driver
    appro_page = ApprovalPage(driver=driver)
    appro_page.log.info('--[普通员工登录]')
    result = appro_page.login_ordinary_staff()
    assert result is not True, '登录失败！'









