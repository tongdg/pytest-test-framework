#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-10 Created by tongdg'

from ykb.pc.bill_page import BillPage
from selenium.webdriver.common.action_chains import ActionChains
import time

class ApprovalPage(BillPage):

    """
        头部：等待审批 审批记录 关键字 搜索按钮
        中部： 勾选 最后更新 提单日期 人员 类别 摘要 金额（元） 应付金额（元） 处理状态
        单据部分：
    """

    """
        所有列表公用,搜索模块
    """
    # 输入关键字
    @property
    def list_input_keyword(self):
        return self.find_element_by_css_ykb("input[class='condition']")
    # 搜索按钮
    @property
    def list_keyword_search(self):
        return self.find_element_by_css_ykb("span[class='btnSearch']")
    # 所有单据
    @property
    def list_all_bills(self):
        return self.find_element_by_link_text_ykb('所有单据')
    # 新单据审批中frame
    @property
    def get_new_main_frame(self):
        return self.find_element_by_id_ykb('newMainIframe')

    """
        我的审批列表，业务审批列表
    """
    # 头部导航条
    # 等待审批
    @property
    def list_approval_wait(self):
        return self.find_element_by_link_text_ykb('等待审批')
    # 审批记录
    @property
    def list_approval_recored(self):
        return self.find_element_by_link_text_ykb('审批记录')
    # 中部导航条
    # 找出所有的td的集合
    @property
    def list_middle_navigation_bar(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_id('MyDraft_Header').find_elements_by_tag_name('td')
        )
    # 单据列表
    # 找出所有的tr的集合
    @property
    def list_approval_bills(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('myBusinessApprvalTask').find_elements_by_tag_name('tr')
        )
    """
        财务审核 报销列表 借款列表 
    """
    # 等待审核
    @property
    def list_to_examine_wait(self):
        return self.find_element_by_link_text_ykb('等待审核')
    # 审核记录
    @property
    def list_to_examine_record(self):
        return self.find_element_by_link_text_ykb('审核记录')
    # 财务审核借款单据列表
    # 找出所有的tr的集合
    @property
    def list_to_examine_loan_bills(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_id('myFinanceLoanVerifyTask').find_elements_by_tag_name('tr')
        )
    # 输入单据号，判断是否找到单据的依据
    @property
    def list_find_examine_loan_bill_flag(self):
        return self.find_element_by_hierarchy(
            lambda var : self.list_to_examine_loan_bills[0].find_element_by_css_selector("input[type='checkbox']")
        )

    # 财务审核报销单据列表
    # 找出所有的tr的集合
    @property
    def list_to_examine_reimbursement_bills(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('myReimbursementVerifyTask').find_elements_by_tag_name('tr')
        )
    # 输入单据号，判断是否找到单据的依据
    @property
    def list_find_examine_reimbursement_bill_flag(self):
        return self.find_element_by_hierarchy(
            lambda var: self.list_to_examine_reimbursement_bills[0].find_element_by_css_selector("input[type='checkbox']")
        )

    # 加审同意按钮
    @property
    def add_approval_person_agree(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-direct-agree']")
    # 新单据财务选择审批人列表
    @property
    def new_approval_person_list(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_css_selector(
                "#fixedFoot > div:nth-child(3) > form > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div.panelscoll"
            ).find_elements_by_tag_name('label')
        )
    # 新单据财务选择审批人列表，确定按钮
    @property
    def new_approval_person_list_confirm(self):
        return self.find_element_by_css_ykb('#fixedFoot > div:nth-child(3) > form > div > div > button.btn.themebgStyle.pull-right')
    # 加审确定按钮
    @property
    def new_add_approval_confirm_button(self):
        return self.find_element_by_id_ykb('countersignBtr')
    """
        财务复核 报销列表 借款列表
    """
    # 等待复核
    @property
    def list_to_review_wait(self):
        return self.find_element_by_link_text_ykb('等待复核')
    # 审核记录
    def list_to_review_record(self):
        return self.find_element_by_link_text_ykb('复核记录')
    # 财务复核单据列表
    # 找出所有的tr的集合
    @property
    def list_to_review_loan_bills(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('myFinanceLoanReviewTask').find_elements_by_tag_name('tr')
        )
    # 输入单据号，判断是否找到单据的依据
    @property
    def list_find_review_loan_bill_flag(self):
        return self.find_element_by_hierarchy(
            lambda var: self.list_to_review_loan_bills[0].find_element_by_css_selector("input[type='checkbox']")
        )
    # 财务复核单据列表
    # 找出所有的tr的集合
    @property
    def list_to_review_reimbursement_bills(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('tblMyReimbursementReviewTask').find_elements_by_tag_name('tr')
        )
    # 输入单据号，判断是否找到单据的依据
    @property
    def list_find_review_reimbursement_bill_flag(self):
        return self.find_element_by_hierarchy(
            lambda var: self.list_to_review_reimbursement_bills[0].find_element_by_css_selector("input[type='checkbox']")
        )

    # 新单据复核选择审批人列表
    @property
    def new_approval_person_review_list(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector(
                "#fixedFoot > div:nth-child(2) > form > div.form-group.sp-el > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div.panelscoll"
            ).find_elements_by_tag_name('label')

        )
    # 新单据财务选择审批人列表，确定按钮
    @property
    def new_approval_person_review_list_confirm(self):
        return self.find_element_by_css_ykb(
            '#fixedFoot > div:nth-child(2) > form > div.form-group.sp-el > div > button.btn.themebgStyle.pull-right')
    """
        出纳 付款 收款
    """
    # 等待付款
    @property
    def list_payment_wait(self):
        return self.find_element_by_link_text_ykb('等待付款')
    # 支付
    @property
    def old_payment_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-direct-agree']")
    # 出纳支付单据列表
    # 找出所有的tr的集合
    @property
    def list_to_payment_bills(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('myPaymentTask').find_elements_by_tag_name('tr')
        )
    # 输入单据号，判断是否找到单据的依据
    @property
    def list_find_payment_bill_flag(self):
        return self.find_element_by_hierarchy(
            lambda var: self.list_to_payment_bills[0].find_element_by_css_selector("input[type='checkbox']")
        )
    """
        新老单据通用
    """
    # 老单据审批记录按钮
    @property
    def approval_record_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-approvedtrace']")
    # 新单据审批记录按钮
    @property
    def new_apporval_record_button(self):
        return self.find_element_by_css_ykb('#fixedFoot > div.cp7.clearfix > button:nth-child(5)')
    # 会签展开按钮 workflow-hq-icon workflow-hq-iconed
    @property
    def open_countersign(self):
        return self.find_element_by_css_ykb("span[class='workflow-hq-icon handTabHq workflow-hq-iconed']")
    # 审批状态
    @property
    def approval_status(self):
        return self.find_element_by_hierarchy(
            lambda var : self.driver.find_element_by_css_selector("span[class='workflow-status']").find_element_by_tag_name('b')
        )
    # 新单据会签展开按钮  workflow-hq-icon workflow-hq-iconed
    @property
    def new_open_countersign(self):
        return self.find_element_by_css_ykb("span[class='workflow-hq-icon workflow-hq-iconed']")
    # 审批记录关闭按钮
    @property
    def apporval_record_close_button(self):
        return self.find_element_by_css_ykb("#mainform > div.modal.fade.in > div > div > div.modal-footer > button")
    # 老单据审批记录关闭按钮
    @property
    def old_apporval_record_close_button(self):
        return self.find_element_by_css_ykb("button[class='btn btn-default']")
    # 审批人列表
    @property
    def old_approval_person_list(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_id('e7ccplugincombobox_AZ').find_elements_by_tag_name('label')
        )
    # 选择审批人列表确定按钮  eui-btn eui-btn-blue btn-save
    @property
    def old_approval_person_list_confirm(self):
        return self.find_element_by_css_ykb("input[class='eui-btn eui-btn-blue btn-save']")
    # 选择审批人的输入框
    @property
    def old_approval_input2(self):
        return self.find_element_by_css_ykb("input[class='approval-selector ldry']")
    # 出纳支付按钮
    @property
    def new_payment_button(self):
        return self.find_element_by_id_ykb('zhifuBtr')
    """
        老单据 同意 退回 返回 加审
    """
    # 同意按钮
    @property
    def old_approval_agree(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-agree']")
    # 退回按钮
    @property
    def old_approval_reject(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-red btn-reject']")
    # 确定按钮
    @property
    def old_approval_confirm(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-approval-confirm']")
    # 返回按钮
    @property
    def old_approval_back(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey btn-back']")
    # 财务加审
    @property
    def old_add_approval(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-addprocess']")
    """
        通用方法
    """
    # 等待错误弹窗消失
    def wait_element_disappear_messager_error(self):
        return self.wait_element_disappear_true("div[class='messager error']",0.05)
    # 等待正确弹窗消失
    def wait_element_disappear_messager_success(self):
        return self.wait_element_disappear_true("div[class='messager success']",0.05)
    # 等待老单据审批处理中
    def wait_element_disappear_old_in_handle(self):
        return self.wait_element_disappear_true("button[class='eui-btn eui-btn-blue btn-approval-confirm disabled']")
    # 等待支付处理中的单子
    def wait_element_disappear_old_in_payment(self):
        return self.wait_element_disappear_true("button[class='eui-btn eui-btn-blue btn-direct-agree disabled']")
    # 商旅订单下单确定按钮
    @property
    def business_travel_confirm_btn(self):
        return self.find_element_by_css_ykb('#message-check > div > div > div.confirm-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm',3)
    """
        老单据
    """

    # 进入我的审批列表
    def __enter_approval_list(self):
        time.sleep(1)
        # 点击我的审批列表
        self.click(self.my_approva_link)
        time.sleep(1)
    # 找到单据，进到单据页面
    def __find_old_bill(self):
        time.sleep(1)
        # 点击等待审批列表，确定当前列表正确
        self.click(self.list_approval_wait)
        # 等待数据加载
        self.wait_element_disappear_data_load()
        # 输入单据号
        self.send_keys(self.list_input_keyword,self.bill_number)
        time.sleep(1)
        # 搜索
        self.click(self.list_keyword_search)
        time.sleep(2)
        # 判断提单的单据号是否与当前单据号一致
        if self.old_bill_number is not False:
            if self.bill_number == self.old_bill_number.text:
                self.log.debug('--[ 单据查找正确]')
                return True
            else:
                self.log.debug('--[ 单据查找错误]')
                return False
        else:
            self.log.debug('--[ 单据查找不到]')
            return False
    # 进入审批列表，找到提交的单据
    def enter_list_find_old_bill(self):
        self.__enter_approval_list()
        return self.__find_old_bill()
    # 判断当前流程是否正确
    def judge_approval_process(self,process):
        time.sleep(1)
        self.click(self.approval_record_button)
        time.sleep(1)
        self.wait_element_disappear_data_load()
        if '会签中' in self.approval_status.text:
            self.click(self.open_countersign)
            time.sleep(1)
        if process in self.approval_status.text:
            self.log.debug('--[审批状态正确]')
            self.click(self.old_apporval_record_close_button)
            return True
        else:
            self.log.debug('--[审批状态错误]')
            return False
    # 审批单子
    def approval_old_agree(self,appro_person):
        time.sleep(1)
        self.click(self.old_approval_agree)
        time.sleep(1)
        # 判断下一个审批人是否正确，断言
        opis = []
        if self.old_approval_input is not False:
            for opi in self.old_approval_input:
                opis.append(opi.get_attribute('textContent'))
            if set(appro_person) <= set(opis):
                self.log.debug('--[ 下一个环节审批领导带出正确]')
                return True
            else:
                self.log.debug('--[ 下一个环节审批领导带出错误]')
                return False
        else:
            self.log.debug('--[ 下一个环节没有审批领导]')
            return True
    # 确定审批过去
    def old_apply_confirm(self):
        time.sleep(1)
        self.click(self.old_approval_confirm)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']",15)
        self.wait_element_disappear_messager_success()
        if messager_success is True:
            self.log.debug('--[ 单据审批成功]')
            return True
        else:
            if self.business_travel_confirm_btn is not False:
                self.click(self.business_travel_confirm_btn)
                messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
                if messager_success is True:
                    self.log.debug('--[ 单据审批成功]')
                    return True
                else:
                    self.log.debug('--[ 单据审批失败]')
                    return False
            else:
                self.log.debug('--[ 单据审批失败]')
                return False
    # 审批加审单子
    def add_approval_old_agree(self):
        time.sleep(1)
        self.click(self.add_approval_person_agree)
        time.sleep(1)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
        self.wait_element_disappear_messager_success()
        if messager_success is True:
            self.log.debug('--[ 单据审批成功]')
            return True
        else:
            self.log.debug('--[ 单据审批失败]')
            return False

    # 进入财务借款列表
    def __enter_finance_loan_list(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.finance).perform()
        ActionChains(self.driver).move_to_element(self.to_examine).perform()
        time.sleep(1)
        self.click(self.to_examine_loan[0])
        time.sleep(1)

    # 财务借款等待审核列表,找到借款单
    def __find_finance_loan(self):
        time.sleep(1)
        self.click(self.list_to_examine_wait)
        time.sleep(1)
        # 输入单据号搜索
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 点击搜索按钮
        self.click(self.list_keyword_search)
        time.sleep(1)
        flag = self.list_find_examine_loan_bill_flag
        lab = self.list_to_examine_loan_bills
        if flag is not False:
            self.log.debug('--[ 单据查找ok]')
            self.click(lab[0])
            return True
        else:
            self.log.debug('--[ 单据查找失败]')
            return False
    # 进入财务借款等待审核列表,找到借款单
    def enter_list_find_finance_loan(self):
        # 进入审核借款页面
        self.__enter_finance_loan_list()
        # 找到借款单
        return self.__find_finance_loan()

    # 进入财务借款列表
    def __enter_review_loan_list(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.finance).perform()
        ActionChains(self.driver).move_to_element(self.to_review).perform()
        time.sleep(1)
        self.click(self.to_review_loan[0])
        time.sleep(1)
    # 财务借款等待复核列表,找到借款单
    def __find_review_loan(self):
        time.sleep(1)
        self.click(self.list_to_review_wait)
        time.sleep(1)
        # 输入单据号搜索
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 点击搜索按钮
        self.click(self.list_keyword_search)
        time.sleep(1)
        self.wait_element_disappear_data_load()
        flag = self.list_find_review_loan_bill_flag
        lab = self.list_to_review_loan_bills
        if flag is not False:
            self.log.debug('--[ 单据查找ok]')
            self.click(lab[0])
            return True
        else:
            self.log.debug('--[ 单据查找失败]')
            return False
    # 进入财务借款等待复核列表,找到借款单
    def enter_list_find_review_loan(self):
        self.__enter_review_loan_list()
        return self.__find_review_loan()

    # 进入出纳付款列表
    def __enter_payment_list(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.cashier).perform()
        self.click(self.payment)
        time.sleep(1)

    # 出纳付款等待付款列表,找到借款单
    def __find_payment(self,bill_type):
        time.sleep(1)
        self.click(self.list_payment_wait)
        time.sleep(1)
        # 输入单据号搜索
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 点击搜索按钮
        self.click(self.list_keyword_search)
        time.sleep(1)
        flag = self.list_find_payment_bill_flag
        lab = self.list_to_payment_bills
        if flag is not False:
            self.log.debug('--[ 单据查找ok]')
            self.click(lab[0])
            if bill_type == 'new':
                time.sleep(1)
                self.driver.switch_to.frame(self.get_new_main_frame)
            return True
        else:
            self.log.debug('--[ 单据查找失败]')
            return False
    # 进入出纳付款等待付款列表,找到借款单
    def enter_list_find_payment(self,bill_type='old'):
        self.__enter_payment_list()
        return self.__find_payment(bill_type)
    # 借款申请单支付
    def old_payment(self):
        time.sleep(1)
        self.click(self.old_payment_button)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
        self.wait_element_disappear_old_in_payment()
        if messager_success is True:
            self.log.debug('--[ 支付成功]')
            return True
        else:
            self.log.debug('--[ 支付失败]')
            return False

    # 老单据加审操作
    def __add_opproval_loan(self,approval_person):
        time.sleep(1)
        self.click(self.old_approval_input2)
        time.sleep(1)
        oapls = self.old_approval_person_list
        for oapl in oapls:
            if oapl.text in approval_person:
                self.click(oapl)
                time.sleep(1)
        self.click(self.old_approval_person_list_confirm)
        time.sleep(1)

    # 财务加审确定
    def add_financial_approval_cofirm_loan(self,approval_person='加审领导'):
        # 点击加审按钮
        time.sleep(1)
        self.click(self.old_add_approval)
        self.__add_opproval_loan(approval_person)
        return self.old_apply_confirm()

    # 老单据加审操作
    def add_old_approval_confirm_loan(self,approval_person):
        self.__add_opproval_loan(approval_person)
        return self.old_apply_confirm()

    """
        新单据
    """
    # 找到新单据断言
    def __find_new_bill(self):
        time.sleep(1)
        # 点击等待审批列表，确定当前列表正确
        self.click(self.list_approval_wait)
        # 等待数据加载
        self.wait_element_disappear_data_load()
        # 输入单据号
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 搜索
        self.click(self.list_keyword_search)
        time.sleep(2)
        # 切到审批的单据中
        self.wait_element_disappear_data_load()
        try:
            self.driver.switch_to.frame(self.get_new_main_frame)
            time.sleep(1)
            if self.new_bill_number is not False:
                if self.bill_number == self.new_bill_number.text:
                    self.log.debug('--[ 单据查找正确]')
                    return True
                else:
                    self.log.debug('--[ 单据查找错误]')
                    return False
            else:
                self.log.debug('--[ 单据查找不到]')
                return False
        except Exception as e:
            self.log.error('--[错误信息是：'+ e +']')
            self.log.debug('--[ 单据查找不到]')
            return False


    # 进入我的审批列表，找到单据，判断
    def enter_list_find_new_bill(self):
        self.__enter_approval_list()
        return self.__find_new_bill()

    # 判断当前流程是否正确
    def judge_new_approval_process(self,process,bill_type='old'):
        time.sleep(1)
        self.click(self.new_apporval_record_button)
        time.sleep(1)
        if '会签中' in self.approval_status.text:
            if bill_type == 'old':
                self.click(self.open_countersign)
                time.sleep(1)
            elif bill_type == 'new':
                self.click(self.new_open_countersign)
                time.sleep(1)
        if process in self.approval_status.text:
            self.log.debug('--[ 审批状态正确]')
            self.click(self.apporval_record_close_button)
            return True
        else:
            return False

    # 同意，判断下一个流程是否正确
    def approval_new_agree(self,appro_person=''):
        time.sleep(1)
        self.click(self.new_bill_agree_button)
        time.sleep(1)
        # 判断下一个审批人是否正确，断言  get_attribute('textContent')
        if self.new_approval_input is not False and self.new_approval_input.text != '':
            if appro_person == self.new_approval_input.text:
                self.log.debug('--[ 下一个环节审批领导带出正确]')
                return True
            else:
                self.log.debug('--[ 下一个环节审批领导带出错误]')
                return False
        else:
            self.log.debug('--[ 下一个环节没有审批领导]')
            return True
    # 费用报销单同意，判断是否提交成功
    def new_bill_confirm_approval(self):
        time.sleep(1)
        self.click(self.new_bill_agree_button2)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
        self.wait_element_disappear_messager_success()
        if messager_success is True:
            self.log.debug('--[ 单据审批成功]')
            return True
        else:
            self.log.debug('--[ 单据审批失败]')
            return False

    # 进入财务审核报销列表
    def __enter_finance_reimbursement_list(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.finance).perform()
        ActionChains(self.driver).move_to_element(self.to_examine).perform()
        time.sleep(1)
        self.click(self.to_examine_reimbursement[1])
        time.sleep(1)
    # 财务审核报销等待审核列表
    def __find_finance_reimbursement(self):
        time.sleep(1)
        self.click(self.list_to_examine_wait)
        time.sleep(1)
        self.wait_element_disappear_data_load()
        time.sleep(1)
        # self.bill_number = 'DC190617192020074'
        # 输入单据号搜索
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 点击搜索按钮
        self.click(self.list_keyword_search)
        time.sleep(1)
        flag = self.list_find_examine_reimbursement_bill_flag
        lab = self.list_to_examine_reimbursement_bills
        if flag is not False:
            self.log.debug('--[ 单据查找ok]')
            self.click(lab[0])
            # 切到审批的单据中
            time.sleep(1)
            self.driver.switch_to.frame(self.get_new_main_frame)
            return True
        else:
            self.log.debug('--[ 单据查找失败]')
            return False
    # 进入财务审核报销等待审核列表，找到报销单
    def enter_list_find_finance_reimbursement(self):
        self.__enter_finance_reimbursement_list()
        return self.__find_finance_reimbursement()

    # 进入财务复核报销列表
    def __enter_review_reimbursement_list(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.finance).perform()
        ActionChains(self.driver).move_to_element(self.to_review).perform()
        time.sleep(1)
        self.click(self.to_examine_reimbursement[1])
        time.sleep(1)
    # 财务审核复核等待审核列表
    def __find_review_reimbursement(self):
        time.sleep(1)
        self.click(self.list_to_review_wait)
        time.sleep(1)
        self.wait_element_disappear_data_load()
        time.sleep(1)
        # 输入单据号搜索
        self.send_keys(self.list_input_keyword, self.bill_number)
        time.sleep(1)
        # 点击搜索按钮
        self.click(self.list_keyword_search)
        self.wait_element_disappear_data_load()
        flag = self.list_find_review_reimbursement_bill_flag
        lab = self.list_to_review_reimbursement_bills
        if flag is not False:
            self.log.debug('--[ 单据查找ok]')
            self.click(lab[0])
            # 切到审批的单据中
            time.sleep(1)
            self.driver.switch_to.frame(self.get_new_main_frame)
            return True
        else:
            self.log.debug('--[ 单据查找失败]')
            return False
    # 进入财务复核报销等待审核列表，找到报销单
    def enter_list_find_review_reimbursement(self):
        self.__enter_review_reimbursement_list()
        return self.__find_review_reimbursement()

    # 新单据支付
    def new_payment(self):
        time.sleep(1)
        self.click(self.new_payment_button)
        messager_success = self.judge_js_pop_exist_visible("div[class='messager success']")
        self.wait_element_disappear_old_in_payment()
        if messager_success is True:
            self.log.debug('--[ 支付或者审批成功]')
            return True
        else:
            self.log.debug('--[ 支付或者审批失败]')
            return False
    # 新单据财务环节添加审批人,确定
    def add_approval_finance_confirm(self,approval_person='加审领导'):
        time.sleep(1)
        self.click(self.new_finance_add_approval_button)
        time.sleep(1)
        self.click( self.new_finance_approval_input)
        time.sleep(1)
        napls = self.new_approval_person_list
        for napl in napls:
            if napl.text in approval_person:
                self.click(napl)
                time.sleep(1)
        self.click(self.new_approval_person_list_confirm)
        time.sleep(1)
        self.click(self.new_add_approval_confirm_button)
        return True
    # 新单据复核环节添加审批人,确定
    def add_approval_person_review_confirm(self,approval_person='财务总监'):
        time.sleep(1)
        self.click(self.new_approval_input)
        time.sleep(1)
        napls = self.new_approval_person_review_list
        for napl in napls:
            if napl.text in approval_person:
                self.click(napl)
                time.sleep(1)
        self.click(self.new_approval_person_review_list_confirm)
        time.sleep(1)
        return self.new_bill_confirm_approval()



























































































