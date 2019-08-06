#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-04 Created by tongdg'

from pages.pc_pages.index_page import IndexPage
import time
from common.utils import Utils
from selenium.webdriver.common.action_chains import ActionChains

Utils = utils = Utils()
import sys

sys.setrecursionlimit(100000)  # 设置最大递归深度
from pages.pc_pages.business_travel_page import BusinessTravelPage


class BillPage(IndexPage):
    """
    页面元素
    1.出差申请单
    2.采购申请单
    3.借款申请单
    4.差旅报销单
    5.费用报销单
    """

    '''
        出差申请单
    '''

    # 出差申请单
    @property
    def evection_apply_bill(self):
        return self.find_element_by_css_ykb("h4[class='eui-form-title']")

    # 出差单据号
    @property
    def old_bill_number(self):
        return self.find_element_by_css_ykb("div[e7id='SerialNumber']")

    # 出差日期
    @property
    def evection_date(self):
        return self.find_element_by_css_ykb(
            '#tb > tbody > tr.row-1 > td.date.td-date.cell-value-1 > input:nth-child(2)')

    # 时间控件,获取所有的有效的天数，去第三个点击就ok
    @property
    def time_contro_day(self):
        return self.find_elements_by_css_ykb("td[class='day']")

    # 出差出发地点
    @property
    def evection_start_place(self):
        return self.find_element_by_css_ykb('#tb > tbody > tr.row-1 > td:nth-child(4) > input')

    # 选择地点控件
    @property
    def evection_place_control(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector("div[class='item']").find_elements_by_tag_name('a'))

    # 出差到达地点
    @property
    def evection_arrive_place(self):
        return self.find_element_by_css_ykb('#tb > tbody > tr.row-1 > td:nth-child(6) > input')

    # 出差费用归属
    @property
    def evection_cost_belong(self):
        return self.find_element_by_css_ykb("td[class='td-department cell-value-1']")

    # 选择部门
    @property
    def evection_choose_department(self):
        return self.find_elements_by_class_name_ykb('t-a-l')[0]

    # 部门列表
    @property
    def evection_department_list(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            "#e7ccplugincombobox_AZ > ul > li > div > ul").find_elements_by_tag_name('a'))

    # 选择项目
    @property
    def evection_choose_project(self):
        return self.find_elements_by_class_name_ykb('t-a-l')[1]

    # 项目列表
    @property
    def evection_project_list(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            "#e7ccplugincombobox_AZ > ul > li > div > ul").find_elements_by_tag_name('a'))

    # 确定按钮
    @property
    def evection_cost_belong_confirm(self):
        return self.find_element_by_css_ykb("button[class='btn btn-primary commit']")

    # 出差交通工具
    @property
    def evection_vehicle(self):
        return self.find_element_by_css_ykb("input[e7id='TransportType']")

    # 交通工具列表
    @property
    def evection_vehicle_list(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            "#e7ccplugincombobox_AZ > ul > li > div > ul").find_elements_by_tag_name('a'))

    # 选择航班
    @property
    def choose_flight_btn(self):
        return self.find_element_by_css_ykb("button[class='colSky gotoConsumption']")

    # 选择酒店
    @property
    def choose_hotel_btn(self):
        return self.find_element_by_css_ykb('#hotel_goto > button')

    # 出差同行人员
    @property
    def evection_colleague_personnel(self):
        return self.find_element_by_css_ykb("td[class='td-field cell-value']")

    # 出差事由
    @property
    def evection_cause(self):
        return self.find_element_by_css_ykb("textarea[e7id='Memo']")

    """
        借款申请单
    """

    # 借款申请单
    @property
    def loan_apply_bill(self):
        return self.find_element_by_css_ykb("h4[class='eui-form-title']")

    # 借款金额
    @property
    def loan_price(self):
        return self.find_element_by_css_ykb("input[e7id='Amount']")

    # 借款事由
    @property
    def loan_cause(self):
        return self.find_element_by_css_ykb("textarea[e7id='Memo']")

    """
        老单据通用
    """

    # 提交审批按钮
    @property
    def old_submit_approval(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-commit']")

    # 勾选会签按钮
    @property
    def old_countersign_button(self):
        return self.find_element_by_id_ykb('chkPm')

    # 会签输入框
    @property
    def old_countersign_input(self):
        return self.find_element_by_css_ykb('#checkHqBtn > div > input')

    # 勾选审批按钮
    @property
    def old_approval_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-commit']")

    # 审批人员  "span[e7id='Superior']"
    @property
    def old_approval_input(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector("span[e7id='Superior']").find_elements_by_tag_name(
                'span'), 3)

    # 老单据确认按钮,点击确定后变为eui-btn eui-btn-blue btn-commit-confirm disabled
    @property
    def old_cofirm_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-commit-confirm']")

    # 老单据返回按钮
    @property
    def old_return_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey btn-commit-cancel']")

    # 上传附件
    @property
    def old_upload_enclosure_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-upload']")

    # 保存按钮
    @property
    def old_save(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-save']")

    # 打印
    @property
    def old_print(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-grey2 btn-print']")

    '''
        采购申请单
    '''

    # 采购申请单
    @property
    def purchase_apply_bill(self):
        return self.find_element_by_partial_link_text_ykb('采购申请单')

    # 费用名称
    @property
    def purchase_cost_name(self):
        return self.find_element_by_id_ykb('subjectName')

    # 采购说明
    @property
    def purchase_explain(self):
        return self.find_element_by_id_ykb('exampleMemo')

    # 商场采购
    @property
    def purchase_shop(self):
        return self.find_element_by_class_name_ykb('themeStyle')

    # 提交审批按钮
    @property
    def new_submit_approval(self):
        return self.find_element_by_id_ykb('commitBtr')

    # 勾选会签按钮
    @property
    def new_countersign_button(self):
        return self.find_element_by_css_ykb("label[class='checkboxs le5 checkedboxs']")

    # 会签输入框
    @property
    def new_countersign_input(self):
        return self.find_element_by_css_ykb("span[class='spanLine ckdropd']")

    # 勾选审批领导按钮
    @property
    def new_approval_button(self):
        return self.find_element_by_css_ykb("label[class='checkboxs le5']")

    # 审批领导输入框 #fixedFoot > div:nth-child(2) > form > div.form-group.sp-el > span
    @property
    def new_approval_input(self):
        return self.find_element_by_css_ykb("#fixedFoot > div:nth-child(2) > form > div.form-group.sp-el > span")

    # 财务加审按钮
    @property
    def new_finance_add_approval_button(self):
        return self.find_element_by_css_ykb('#fixedFoot > div.cp7.clearfix > button.btn.btn-defaul.t2')

    # 财务加审领导输入框
    @property
    def new_finance_approval_input(self):
        return self.find_element_by_css_ykb('#fixedFoot > div:nth-child(3) > form > div > span')

    """
        差旅报销单
    """

    # 差旅报销单
    @property
    def travel_reimbursement_bill(self):
        return self.find_element_by_tag_name_ykb('h1')

    # 摘要
    @property
    def travel_abstract(self):
        return self.find_element_by_id_ykb('exampleMemo')

    # 差旅报销单确认按钮
    @property
    def travel_confirm_button(self):
        return self.find_element_by_css_ykb("button[class='btn themebgStyle pull-right mt18']")

    """
        行列用法： td        td          td          td        td        td        td       td
            tr 行程说明    城际交通     酒店住宿    市内交通    其它费用    出差补助   费用小计   费用归属
            tr 行程说明    城际交通     酒店住宿    市内交通    其它费用    出差补助   费用小计   费用归属
            需要注意的是: 获取到的td元素需要获取到下面能用的元素，不能直接用，可能输入值或者点击无效。
            需要特殊处理的行 行程说明
    """

    # 现有单据的所有行
    @property
    def travel_row(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector('#traTable > tbody').find_elements_by_tag_name('tr'))

    # 现有单据的第N行的第几列
    def travel_row_column(self, n, m):
        return self.find_element_by_hierarchy(lambda var: self.travel_row[n].find_elements_by_tag_name('td')[m])

    # 特殊处理的第几行第几列的行程说明
    def travel_row_colum_trip_explain(self, n, m):
        return self.find_element_by_hierarchy(
            lambda var: self.travel_row_column(n, m).find_element_by_tag_name('textarea'))

    # 填写城际交通  第二列
    def travel_intercity_traffic(self, n):
        return self.travel_row_column(n, 1)

    # 获取城际交通填写页面所有行
    @property
    def travel_intercity_traffic_tbody(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector('#chjiList > table > tbody').find_elements_by_tag_name(
                'tr'))

    # 城际交通填写页面的第N行的第几列
    def travel_intercity_traffic_row_column(self, n, m):
        return self.find_element_by_hierarchy(
            lambda var: self.travel_intercity_traffic_tbody[n].find_elements_by_tag_name('td')[m])

    # 特殊处理 金额的填写
    @property
    def travel_intercity_traffic_price(self):
        return self.find_element_by_hierarchy(
            lambda var: self.travel_intercity_traffic_row_column(0, 5).find_element_by_css_selector(
                "input[class='nobg text-right']"))

    # 城际交通确定按钮
    @property
    def travel_intercity_traffic_confirm_button(self):
        return self.find_element_by_css_ykb(
            '#mainform > div.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary')

    # 城际交通的交通工具
    @property
    def travel_intercity_traffic_vehicle(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            '#chjiList > table > tbody > tr:nth-child(1) > td.dpselect > div > div > div > ul').find_elements_by_tag_name(
            'li'))

    # 城际交通地点控件
    @property
    def travel_intercity_traffic_palace_control(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            '#app > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(2) > ul').find_elements_by_tag_name(
            'li'))

    # 填写酒店住宿  第三列
    def travel_hotel_stay(self, n):
        return self.travel_row_column(n, 2)

    # 填写市内交通  第四列
    def travel_city_traffic(self, n):
        return self.travel_row_column(n, 3)

    # 填写其他费用 第五列
    def travel_other_cost(self, n):
        return self.travel_row_column(n, 4)

    # 填写出差补助 第六列
    def travel_subsidy(self, n):
        return self.travel_row_column(n, 5)

    # 费用小计
    def travel_cost_subtotal(self, n):
        return self.travel_row_column(n, 6)

    """
        费用报销页面
    """

    # 费用报销单
    @property
    def cost_reimbursement_bill(self):
        return self.find_element_by_tag_name_ykb('h1')

    # 摘要
    @property
    def cost_abstract(self):
        return self.find_element_by_id_ykb('exampleMemo')

    # 费用报销单确认按钮  btn themebgStyle pull-right
    @property
    def cost_confirm_button(self):
        return self.find_element_by_css_ykb('#fixedFoot > div:nth-child(2) > form > span > button:nth-child(2)')

    @property
    def new_bill_agree_button2(self):
        return self.find_element_by_id_ykb('approvalBtr')

    """
        行列用法：  td        td      td     td      td   
            tr  费用名称    费用说明  日期   报销金额  费用归属
            tr  费用名称    费用说明  日期   报销金额  费用归属

    """

    # 费用报销单的所有行
    @property
    def cost_bill_row(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector('#reiTable > tbody').find_elements_by_tag_name('tr'))

    # 费用报销单的第N行的第几列
    def cost_bill_row_column(self, n, m):
        return self.find_element_by_hierarchy(lambda var: self.cost_bill_row[n].find_elements_by_tag_name('td')[m])

    # 费用说明特殊处理
    @property
    def cost_bill_abstract(self):
        return self.find_element_by_hierarchy(
            lambda var: self.cost_bill_row_column(1, 1).find_element_by_tag_name('textarea'))

    # 金额特殊处理
    @property
    def cost_price(self):
        return self.find_element_by_hierarchy(
            lambda var: self.cost_bill_row_column(1, 3).find_element_by_tag_name('input'))

    # 费用名称弹框
    @property
    def cost_query_cost_subject(self):
        return self.find_element_by_css_ykb(
            '#app > div.bzBox3.noBod > table > tbody > tr:nth-child(3) > td:nth-child(2) > div.input-group.inputgroup90 > input')

    # 费用名称列表
    @property
    def cost_name_list(self):
        return self.find_element_by_hierarchy(
            lambda var: self.driver.find_element_by_css_selector(
                '#app > div.bzBox3.noBod > table > tbody > tr:nth-child(3) > td:nth-child(2) > div.panelscoll').find_elements_by_tag_name(
                'label'))

    """
       新单据通用
    """

    # 新单据单据号 #bcTargetNum
    @property
    def new_bill_number(self):
        return self.find_element_by_id_ykb('bcTargetNum')

    # 费用归属
    @property
    def new_cost_belong(self):
        return self.find_element_by_css_ykb("span[class='txtOverhide']")

    # 现有费用归属的所有行
    @property
    def new_cost_belong_row(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            '#shareList > table > tbody').find_elements_by_tag_name('tr'))

    # 现有单据的第N行的第几列
    def new_cost_belong_row_column(self, n, m):
        return self.find_element_by_hierarchy(
            lambda var: self.new_cost_belong_row[n].find_elements_by_tag_name('span')[m])

    # 选择部门,选择项目
    @property
    def new_choose_department_project(self):
        return self.find_element_by_hierarchy(lambda var: self.driver.find_element_by_css_selector(
            "div[class='panelscoll']").find_elements_by_tag_name('label'))

    # 关闭选择框
    @property
    def new_choose_department_project_close(self):
        return self.find_element_by_css_ykb('#btrShareList > div.bzBox3.noBod > button')

        # 新单据费用归属关闭按钮

    @property
    def new_cost_belong_confirm_button(self):
        return self.find_element_by_css_ykb(
            "#mainform > div.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary")

    @property
    def travel_confirm_button(self):
        return self.find_element_by_css_ykb("button[class='btn themebgStyle pull-right mt18']")

    # 新单据返回按钮
    @property
    def new_reture_button(self):
        return self.find_element_by_css_ykb("button[class='btn btn-default pull-right mt18']")

    # 导入消费记录
    @property
    def import_consumption_record(self):
        return self.find_element_by_css_ykb("button[class='btn themebgStyle pull-right']")

    '''
        消费记录页面
    '''

    # 消费记录
    @property
    def consumption_record(self):
        return self.find_element_by_css_ykb("h4[class='modal-title']")

    # 查询消费记录
    @property
    def find_consumption_record(self):
        return self.find_element_by_css_ykb("input[class='form-control']")

    # 获取所有的勾选消费记录按钮
    @property
    def consumption_record_button(self):
        return self.find_elements_by_css_ykb("td[class='checkboxs']")

    # 提交报销按钮
    @property
    def submit_reimbursement_button(self):
        return self.find_element_by_css_ykb("button[class='btn themebgStyle']")

    # 同意按钮  #fixedFoot > div.cp7.clearfix > button:nth-child(7)
    @property
    def new_bill_agree_button(self):
        return self.find_element_by_css_ykb('#fixedFoot > div.cp7.clearfix > button:nth-child(7)')

    # 查看发票按钮
    @property
    def see_invoice_button(self):
        return self.find_element_by_id_ykb('checkInvoice')

    # 上传附件按钮  saveNewBtr
    @property
    def new_upload_enclosure_button(self):
        return self.find_element_by_css_ykb("button[class='btn btn-default2 pull-right']")

    # 保存按钮
    @property
    def new_save_button(self):
        return self.find_element_by_id_ykb("saveNewBtr")

    # 打印按钮
    @property
    def new_print(self):
        return self.find_element_by_css_ykb("button[class='btn btn-default2 pull-right']")

    """
        通用模块
    """

    # 等待元素消失
    # 单据数据加载弹窗  'div[class="messager progress-bar2"]'
    # 脚本模块
    def wait_element_disappear_data_load(self):
        self.wait_element_disappear_true('div[class="messager progress-bar2"]', 0.1)

    # 老单据提交状态中按钮,元素改变了
    def wait_element_disappear_old_in_approval_btn(self):
        self.wait_element_disappear_true("button[class='eui-btn eui-btn-blue btn-commit-confirm disabled']")

    # 差旅报销单提交中  "button[class='btn themebgStyle disabled']" 元素没变
    def wait_element_disappear_new_in_approval_btn(self):
        self.wait_element_change_by_text('#commitBtr', '提交附件', 0.1)
        # self.wait_element_disappear_true("button[class='btn themebgStyle disabled']")

    # 费用报销单等待提交
    def wait_element_disappear_new_in_approval_btn2(self):
        self.wait_element_change_by_text('#commitBtr', '提交中', 0.1)

    # 差旅报销单,费用报销单等待提交
    def wait_element_disappear_new_approval_btn(self):
        self.wait_element_change_by_text('#commitBtr', '提交审批', 0.1)

    # 进入出差申请单
    def __enter_evecation_bill_page(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.apply).perform()
        time.sleep(1)
        self.click(self.evection_apply)

    # 费用归属设定
    def __choose_department_projiect(self, department=None, project=None):
        time.sleep(1)
        # 点击费用归属
        self.click(self.evection_cost_belong)
        time.sleep(1)
        # 选择部门  具体的部门从list集合找
        # 判断部门是否传入
        if department is not None:
            # 点击部门，让元素可见
            self.click(self.evection_choose_department)
            time.sleep(1)
            # 获取所有部门的列表
            edls = self.evection_department_list
            # 找出所查找的部门，并点击
            for edl in edls:
                if edl.text == department:
                    self.click(edl)
                    time.sleep(1)
        # 选择项目  具体的项目从list里面找
        # 判断项目是否传入
        if project is not None:
            # 点击项目,让元素可见
            self.click(self.evection_choose_project)
            time.sleep(1)
            # 获取所有项目的列表
            epvs = self.evection_project_list
            # 找出所查找的项目，并点击
            for epv in epvs:
                if epv.text == project:
                    self.click(epv)
                    time.sleep(1)
        # 确认
        self.click(self.evection_cost_belong_confirm)
        time.sleep(2)  # 2S防止点击过快出错

    # 商旅模块
    def run_business(self):
        # 初始化商旅模块
        btp = BusinessTravelPage(self.driver)
        # 选择机票
        self.click(self.choose_flight_btn)
        btp.choose_flight()
        # 选择酒店
        self.click(self.choose_hotel_btn)
        btp.choose_hotel()

    # 填写出差申请单
    def __fill_evection_bill(self, department, project, switch):
        if "出差申请单" not in self.evection_apply_bill.text:
            self.log.debug('--[ open evection bill fail]')
            return False
        else:
            # 记住单据号 唯一标识
            self.bill_number = self.old_bill_number.text
            self.log.debug('--[ ' + self.bill_number + 'open evection bill ok]')
            # 选择日期
            self.click(self.evection_date)
            time.sleep(1)
            # 选择到达日期
            self.click(self.time_contro_day[2])
            time.sleep(1)
            # 出发地点
            self.click(self.evection_start_place)
            time.sleep(1)
            self.click(self.evection_place_control[0])
            time.sleep(1)
            # 到达地点
            self.click(self.evection_arrive_place)
            time.sleep(1)
            self.click(self.evection_place_control[1])
            time.sleep(1)
            # 费用归属设定
            self.__choose_department_projiect(department, project)
            # 选择交通工具
            self.click(self.evection_vehicle)
            time.sleep(1)
            self.click(self.evection_vehicle_list[0])
            time.sleep(1)
            # 同行人暂不加
            # 填写出差事由
            time.sleep(1)
            self.send_keys(self.evection_cause, Utils.generate_time)
            # 判断是否调用商旅模块
            if switch is True:
                self.run_business()
            time.sleep(2)  # 2S防止点击过快出错
            # 选择审批人暂时不加  设置部门负责人和项目负责人
            # 点击确定
            self.click(self.old_approval_button)
            time.sleep(1)
            self.click(self.old_cofirm_button)
            # 等待单据提交
            self.wait_element_disappear_old_in_approval_btn()
            time.sleep(3)  # 3S防止提单的暂时卡住，导致下次填单出错
            return True

    # 进入出差申请单，并且填写单据，提交+
    def enter_fill_evecation_bill(self, department=None, project=None, switch=False):
        # 进入出差申请单
        self.__enter_evecation_bill_page()
        # 填写出差申请单
        return self.__fill_evection_bill(department, project, switch)

    # 进入借款申请单
    def __enter_loan_bill(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.apply).perform()
        time.sleep(1)
        self.click(self.loan_apply)
        time.sleep(1)
        self.wait_element_disappear_data_load()

    # 填写借款申请单
    def __fill_loan_bill(self):
        if "借款单" not in self.loan_apply_bill.text:
            self.log.debug('--[ open loan bill fail]')
            return False
        else:
            self.log.debug('--[ open loan bill ok]')
        # 记住单据号 唯一标识
        self.bill_number = self.old_bill_number.text
        # 输入借款金额1
        self.send_keys(self.loan_price, '1')
        time.sleep(1)
        # 输入借款事由
        self.send_keys(self.loan_cause, Utils.generate_time)
        time.sleep(2)  # 2S防止点击过快出错
        # 提交审批
        while self.driver.find_element_by_css_selector(
                "button[class='eui-btn eui-btn-blue btn-commit']").is_displayed() is False:
            time.sleep(1)
            self.click(self.old_return_button)
            self.log.info('--[ element click too fast to return]')
        self.click(self.old_approval_button)
        # 确定按钮
        time.sleep(1)
        self.click(self.old_cofirm_button)
        # 等待带锯提交
        print(self.driver.find_element_by_css_selector(
            "button[class='eui-btn eui-btn-blue btn-commit-confirm disabled']").is_displayed())
        self.wait_element_disappear_old_in_approval_btn()
        time.sleep(3)  # 3S防止提单的暂时卡住，导致下次填单出错
        return True

    # 进入并且填写借款申请单
    def enter_fill_loan_bill(self):
        # 进入借款申请单
        self.__enter_loan_bill()
        # 填写借款申请单
        return self.__fill_loan_bill()

    """
        新单据 差旅报销单 费用报销单
    """

    # 进入差旅报销单
    def __enter_travel_reimbursement_bill(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.reimbursement).perform()
        time.sleep(1)
        self.click(self.reimbursement_for_travel)
        time.sleep(1)

    # 填写城际交通
    def __fill_travel_intercity_traffic(self):
        # 填写行程说明
        self.send_keys(self.travel_row_colum_trip_explain(1, 0), Utils.generate_time)
        time.sleep(1)
        # 选择交通工具
        self.click(self.travel_intercity_traffic(1))
        time.sleep(1)
        self.click(self.travel_intercity_traffic_row_column(0, 0))
        time.sleep(1)
        # 选择时间
        self.click(self.time_contro_day[0])
        time.sleep(1)
        self.click(self.travel_intercity_traffic_row_column(0, 1))
        time.sleep(1)
        # 选择交通工具
        self.click(self.travel_intercity_traffic_vehicle[0])
        time.sleep(1)
        # 选择出发地点
        self.click(self.travel_intercity_traffic_row_column(0, 2))
        time.sleep(1)
        self.click(self.travel_intercity_traffic_palace_control[0])
        time.sleep(1)
        # 选择到达地点
        self.click(self.travel_intercity_traffic_row_column(0, 3))
        time.sleep(1)
        self.click(self.travel_intercity_traffic_palace_control[1])
        time.sleep(1)
        # 输入金额
        self.send_keys(self.travel_intercity_traffic_price, 1)
        time.sleep(1)
        # 确定
        self.click(self.travel_intercity_traffic_confirm_button)
        time.sleep(2)  # 2S防止过快的点击出错

    # 费用归属
    def __new_choose_cost_belong(self, department, project):
        time.sleep(1)
        # 点击费用归属
        self.click(self.new_cost_belong)
        time.sleep(1)
        # 选择部门
        if department is not None:
            self.click(self.new_cost_belong_row_column(0, 0))
            time.sleep(1)
            ncdps = self.new_choose_department_project
            for ncdp in ncdps:
                if ncdp.text == department:
                    self.click(ncdp)
                    time.sleep(1)
                    break
        # 选择项目
        if project is not None:
            print(project)
            self.click(self.new_cost_belong_row_column(0, 1))
            time.sleep(1)
            ncdps1 = self.new_choose_department_project
            for ncdp1 in ncdps1:
                if ncdp1.text == project:
                    self.click(ncdp1)
                    time.sleep(1)
                    break
        # 费用归属确认按钮
        self.click(self.new_cost_belong_confirm_button)
        time.sleep(2)  # 2S防止过快的点击出错

    # 填写差旅报销单
    def __fill_travel_reimbursement_bill(self, department, project):
        time.sleep(1)
        if "差旅报销单" not in self.travel_reimbursement_bill.text:
            self.log.debug('--[ open travel reimbursement bill fail]')
            return False
        else:
            self.log.debug('--[ open travel reimbursement bill ok]')
            self.send_keys(self.travel_abstract, 'tongdg差旅报销单测试')
            # 记住单据号
            self.bill_number = self.new_bill_number.text
            time.sleep(1)
            # 填写城际交通
            self.__fill_travel_intercity_traffic()
            # 选择费用归属
            self.__new_choose_cost_belong(department, project)
            # 提单
            time.sleep(2)  # 2S防止过快的点击出错
            self.click(self.new_submit_approval)
            time.sleep(2)  # 2S防止过快的点击出错
            # 确定
            self.click(self.travel_confirm_button)
            # 等待单据提交
            self.wait_element_disappear_new_approval_btn()
            if self.wait_element_disappear_new_in_approval_btn() is False:
                self.log.info('--[ 单据提交超时]')
                return False
            else:
                time.sleep(3)  # 3S防止提单的暂时卡住，导致下次填单出错
                return True

    # 进入填写差旅报销单，提交。
    def enter_fill_travel_reimbursement_bill(self, department=None, project=None):
        # 进入差旅报销单
        self.__enter_travel_reimbursement_bill()
        # 填写差旅报销单
        return self.__fill_travel_reimbursement_bill(department, project)

    # 进入费用报销单
    def __enter_cost_bill(self):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.reimbursement).perform()
        time.sleep(1)
        self.click(self.cost_reimbursement)
        time.sleep(1)

    # 填写费用报销单
    def __fill_cost_bill(self, department, project):
        time.sleep(1)
        if "费用报销单" not in self.cost_reimbursement_bill.text:
            self.log.debug('--[ open cost reimbursement bill fail]')
            return False
        else:
            self.log.debug('--[ open cost reimbursement bill ok]')
            time.sleep(1)
            # 记住单据号
            self.bill_number = self.new_bill_number.text
            # 填写摘要
            self.send_keys(self.cost_abstract, 'tongdg测试费用报销单')
            time.sleep(1)
            # 选择费用科目
            self.click(self.cost_bill_row_column(1, 0))
            time.sleep(1)
            self.send_keys(self.cost_query_cost_subject, '备用金')
            time.sleep(2)  # 等待数据加载完
            self.click(self.cost_name_list[0])
            time.sleep(1)
            # 输入说明
            self.send_keys(self.cost_bill_abstract, Utils.generate_time)
            time.sleep(1)
            # 选择日期
            self.click(self.cost_bill_row_column(1, 2))
            time.sleep(1)
            self.click(self.time_contro_day[0])
            time.sleep(1)
            # 输入金额
            self.send_keys(self.cost_price, 1)
            time.sleep(1)
            # 点击费用说明，显示txtOverhide元素
            self.click(self.cost_bill_abstract)
            # 费用归属
            self.__new_choose_cost_belong(department, project)
            self.click(self.new_submit_approval)
            time.sleep(2)  # 2S防止过快的点击出错
            # 确定
            self.click(self.cost_confirm_button)
            # 等待单据提交
            self.wait_element_disappear_new_approval_btn()
            if self.wait_element_disappear_new_in_approval_btn2() is False:
                self.log.info('--[ 单据提交超时]')
                return False
            else:
                time.sleep(3)  # 3S防止提单的暂时卡住，导致下次填单出错
                return True

    # 进入并且填写费用报销单
    def enter_fill_cost_bill(self, department=None, project=None):
        self.__enter_cost_bill()
        return self.__fill_cost_bill(department, project)














































































































