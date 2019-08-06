#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-06-04 Created by tongdg'

from pages.pc_pages.login_page import LoginPage
import time

class IndexPage(LoginPage):
    """
        页面元素
        首页基本元素定位
            1.横向导航条
            1.1
            申请 出差申请单 采购申请单 借款申请单
            报销 差旅报销单 费用报销单
            财务 审核(报销 借款) 复核(报销 借款)
            出纳 付款 收款
            报表 费用分析 预算分析
            更多
            消息
            设置
            退出
            2.纵向导航条
            2.1我的审批 我的单据 我的订单 消费记录 代还欠款 机票 酒店 火车票 采购
    """
    # 首页
    @property
    def home_page(self):
        return self.find_element_by_link_text_ykb('首页')
    '''
        申请 出差申请单 采购申请单 借款申请单
    '''
    # 申请
    @property
    def apply(self):
        return self.find_element_by_link_text_ykb('申请')
    # 出差申请单
    @property
    def evection_apply(self):
        return self.find_element_by_link_text_ykb('出差申请')
    # 采购申请单
    @property
    def purchase_apply(self):
        return self.find_element_by_link_text_ykb('采购申请')
    # 借款申请单
    @property
    def loan_apply(self):
        return self.find_element_by_link_text_ykb('借款申请')

    '''
        报销 差旅报销单 费用报销单
    '''
    # 报销
    @property
    def reimbursement(self):
        return self.find_element_by_link_text_ykb('报销')
    # 差旅报销
    @property
    def reimbursement_for_travel(self):
        return self.find_element_by_link_text_ykb('差旅报销')
    # 费用报销
    @property
    def cost_reimbursement(self):
        return self.find_element_by_link_text_ykb('费用报销')
    '''
        财务 审核(报销 借款)     
    '''
    # 财务
    @property
    def finance(self):
        return self.find_element_by_link_text_ykb('财务')
    # 财务----审核
    @property
    def to_examine(self):
        return self.find_element_by_link_text_ykb('审核')
    # 财务----审核----报销 财务----复核----报销  1,2
    @property
    def to_examine_reimbursement(self):
        return self.find_elements_by_link_text_ykb('报销')
    # 财务----审核----借款 财务----复核----借款  0,1
    @property
    def to_examine_loan(self):
        return self.find_elements_by_link_text_ykb('借款')
    '''
        复核(报销 借款)
    '''
    # 复核
    @property
    def to_review(self):
        return self.find_element_by_link_text_ykb('复核')
    # 报销
    @property
    def to_review_reimbursement(self):
        return self.find_elements_by_link_text_ykb('报销')
    # 借款
    @property
    def to_review_loan(self):
        return self.find_elements_by_link_text_ykb('借款')

    '''
        出纳 付款 收款
    '''
    # 出纳
    @property
    def cashier(self):
        return self.find_element_by_link_text_ykb('出纳')
    # 付款
    @property
    def payment(self):
        return self.find_element_by_link_text_ykb('付款')
    # 收款
    @property
    def receivables(self):
        return self.find_element_by_link_text_ykb('收款')
    '''
        报表 费用分析 预算分析
    '''
    @property
    def report_form(self):
        return self.find_element_by_link_text_ykb('报表')
    # 费用分析
    @property
    def cons_analysis(self):
        return self.find_element_by_link_text_ykb('费用分析')
    # 预算分析
    @property
    def budget_analysis(self):
        return self.find_element_by_link_text_ykb('预算分析')
    # 更多
    @property
    def more(self):
        return self.find_element_by_link_text_ykb('更多')
    # 消息
    @property
    def news(self):
        return self.find_element_by_css_ykb("p[class='updateInform']")
    # 设置
    @property
    def setting(self):
        return self.find_element_by_css_ykb("span[class='btn-setting']")
    # 退出
    @property
    def exit(self):
        return self.find_element_by_css_ykb("span[class='btn-exit']")
    """
        2.我的审批 我的单据 我的订单 消费记录 代还欠款
          机票    酒店     火车票   采购
    """
    # 我的审批
    @property
    def my_approva_link(self):
        return self.find_element_by_link_text_ykb('我的审批')
    # 等待审批
    @property
    def wait_apporva_link(self):
        return self.find_element_by_link_text_ykb('等待审批')
    #审批记录
    @property
    def apporval_record_link(self):
        return self.find_element_by_link_text_ykb('审批记录')
    # 消费记录
    @property
    def consumption_records(self):
        return self.find_element_by_link_text_ykb('消费记录')
    # 剩余借款
    @property
    def arrears(self):
        return self.find_element_by_id_ykb('LoanAmount')
    # 我的单据
    @property
    def my_doucunmens_link(self):
        return self.find_element_by_link_text_ykb('我的单据')
    # 机票
    @property
    def plane_ticket(self):
        return self.find_element_by_class_name_ykb('jipiao')
    # 酒店
    @property
    def hotel(self):
        return self.find_element_by_class_name_ykb('hotel')
    # 火车票
    @property
    def train_ticket(self):
        return self.find_element_by_class_name_ykb('train')
    # 采购
    @property
    def purchase(self):
        return self.find_element_by_class_name_ykb('shop')
    # 当前所在的企业名称
    @property
    def current_enterprise(self):
        return self.find_element_by_css_ykb("span[class='seldropdown']")
    # 获取当前用户名
    @property
    def login_name(self):
        return self.find_element_by_css_ykb(
            '#testApp > div.main > div > div.contentTop > div.boxleft > div.userCenter > div.user > p.name')

    # 切换企业,并且判断当前登录账号是否是传入的值
    def switching_enterprises(self,_enterprise='云快报研发中心',_login_name='童定国'):
        # 判断当前企业是不是等于传入的企业值，若是，不用切换企业；若不是，切换企业
        if self.current_enterprise.text != _enterprise:
            self.click(self.current_enterprise)
            time.sleep(1)
            # 获取菜单栏下面的所有企业
            enterprises = self.find_element_by_hierarchy(lambda var : self.driver.find_element_by_css_selector("ul[class='dropdown-menu dropdown-menuqq']").find_elements_by_tag_name('li'))
            # 判断传入的企业值是否与菜单栏下的企业相等,相等点击
            for enterprise in enterprises:
                if enterprise.text == _enterprise:
                    self.click(enterprise)
                    time.sleep(2)
                    break
                # 判断当前企业是否切换成功
            if self.current_enterprise.text == _enterprise:
                self.log.info('--[switching enterprises ok]')
                # 判断，当前企业的用户名是否正确
                if self.login_name.text == _login_name:
                    self.log.debug('--[login right]')
                    return True
                else:
                    self.log.debug('--[login error]')
                    return False
            else:
                self.log.debug("--[_enterprise find fail]")
                return False
        else:
            self.log.info('--[_enterprise not switching ]')
            # 判断，当前企业的用户名是否正确
            if self.login_name.text == _login_name:
                self.log.debug('--[login right]')
                return True
            else:
                self.log.debug('--[login error]')
                return False
    # 退出操作
    @property
    def sign_out_button(self):
        return self.find_element_by_id_ykb('logout')
    # 确认按钮
    @property
    def confirm_button(self):
        return self.find_element_by_css_ykb("button[class='eui-btn eui-btn-blue btn-modal-confirm']")
    # 退出登录
    def singn_out(self):
        self.click(self.sign_out_button)
        time.sleep(1)
        self.click(self.confirm_button)
        if self.login_btn is False:
            self.log.debug('--[sign out fail]')
            return False
        else:
            self.log.debug('--[sign out ok]')
            return True
