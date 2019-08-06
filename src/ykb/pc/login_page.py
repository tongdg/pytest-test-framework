#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-05-29 Created by tongdg'

from pages.base_page import BasePage
from config import tdg_config
import time
test_address = tdg_config.get_test_address()

class LoginPage(BasePage):
    """
        页面元素
    """
    @property
    def login_btn(self):
        return self.find_element_by_link_text_ykb('登录')
    @property
    def register_btn(self):
        return self.find_element_by_link_text_ykb('免费体验')
    @property
    def username(self):
        return self.find_element_by_id_ykb('LoginName')
    @property
    def password(self):
        return self.find_element_by_id_ykb('Password')
    @property
    def login_btn2(self):
        return self.find_element_by_id_ykb('loginBtn')
    @property
    def login_success_flag(self):
        return self.find_element_by_css_ykb("span[class='seldropdown']")
    """
        我的账号 15216625816 123456 童定国
    """
    def login_test_person(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username,'15216625816')
        time.sleep(1)
        self.send_keys(self.password,'123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ tongdg login fail]')
            return False
        else:
            self.log.debug('--[tongdg ok]')
            return True
    """
        普通员工 16700000001 
    """
    def login_ordinary_staff(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000001')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ ordinary staff fail]')
            return False
        else:
            self.log.debug('--[ ordinarystaff ok]')
            return True
    """
        项目经理 16700000002
    """
    def login_project_manager(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000002')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ ordinary staff fail]')
            return False
        else:
            self.log.debug('--[ ordinarystaff ok]')
            return True
    """
        部门领导 16700000003
    """
    def login_department_leader(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000003')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ department leader fail]')
            return False
        else:
            self.log.debug('--[ department leader ok]')
            return True
    """
        公司领导 16700000004
    """
    def login_company_leader(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000004')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ company leader fail]')
            return False
        else:
            self.log.debug('--[ company leader ok]')
            return True

    """
        会计登录 16700000005
    """
    def login_accounting(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000005')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ accounting leader fail]')
            return False
        else:
            self.log.debug('--[ accounting leader ok]')
            return True

    """
        财务经理 16700000006
    """
    def login_financial_manager(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000006')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ financial manager login fail]')
            return False
        else:
            self.log.debug('--[financial manager login ok]')
            return True
    """
        财务总监 16700000007
    """
    def login_financial_chief_inspector(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000007')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ financial chief inspector login fail]')
            return False
        else:
            self.log.debug('--[ financial chief inspector login ok]')
            return True
    """
        出纳 16700000008
    """
    def login_cashier(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000008')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ financial manager login fail]')
            return False
        else:
            self.log.debug('--[financial manager login ok]')
            return True

    """
        加审领导 16700000009
    """
    def login_add_approval(self):
        self.driver.maximize_window()
        time.sleep(1)
        # 'http://120.132.23.147:840/logon'  'https://www.51ykb.com/Logon'  120.132.23.147:840
        self.driver.get(test_address)
        self.click(self.login_btn)
        time.sleep(1)
        self.send_keys(self.username, '16700000009')
        time.sleep(1)
        self.send_keys(self.password, '123456')
        time.sleep(1)
        self.click(self.login_btn2)
        time.sleep(2)
        # 判断登录是否成功
        if self.login_success_flag is False:
            self.log.debug('--[ add approval login fail]')
            return False
        else:
            self.log.debug('--[ add approval login ok]')
            return True




