#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-23 Created by tongdg'

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from common.logger import Log
from selenium.common.exceptions import TimeoutException,NoSuchElementException,StaleElementReferenceException

class BasePage(object):
    # 存放图片的集合
    # 传入driver和日志路径
    # path传相对路径

    def __init__(self, driver, path=None):
        self.driver = driver
        self.log = Log(path)
    """
        常用定位方法
        1.id,name,class定位，id唯一
        2.link text,partial test定位
    """
    # 每隔0.5秒去查找这个id所对应的元素，超过timeout,单位(s)，抛出TimeoutException.
    # WebDriverWait方法可以设置每隔多少秒扫描，以及找不到抛出的异常类型.
    # 这里需要注意，用显示等待找不到元素抛出的是超时的错误，而直接用find去寻找，返回的是元素找不到的错误，这个以后
    # 判断元素是否找到有很大的作用

    # 元素id定位，唯一标识
    def find_element_by_id_ykb(self, id, timeout=10):
        """
        :param timeout:最长超时时间
        :param id:需要定位的元素的id
        :return:返回找到的元素
        """
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_id(id))
            self.log.info('--[ ' + id + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + id + ' find timeout]')
            return False
    # 元素的name属性定位，不唯一
    def find_element_by_name_ykb(self, name, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_name(name))
            self.log.info('--[ ' + name + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + name + ' find timeout]')
            return False
    # 元素的标签名字定位，不唯一
    def find_element_by_tag_name_ykb(self, tagname, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_tag_name(tagname))
            self.log.info('--[ ' + tagname + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + tagname + ' find timeout]')
            return False
    # 元素class的名字定位，不唯一
    def find_element_by_class_name_ykb(self, classname, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_class_name(classname))
            self.log.info('--[ ' + classname + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + classname + ' find timeout]')
            return False
    def find_elements_by_class_name_ykb(self, classname, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_class_name(classname))
            self.log.info('--[ ' + classname + ' list find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + classname + ' list find timeout]')
            return False
    # 链接的内容定位，也是不唯一的
    def find_element_by_link_text_ykb(self, linktext, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_link_text(linktext))
            self.log.info('--[ ' + linktext + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + linktext + ' find timeout]')
            return False
    # 链接的内容定位，也是不唯一的,返回满足条件的list集合
    def find_elements_by_link_text_ykb(self, linktext, timeout=10):
        try:
            list_ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_link_text(linktext))
            self.log.info('--[ ' + linktext + ' list find ok]' )
            return list_ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + linktext + ' list find timeout]')
            return False
    # 部门链接内容定位，不唯一
    def find_element_by_partial_link_text_ykb(self, partiallinktext, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_partial_link_text(partiallinktext))
            self.log.info('--[ ' + partiallinktext + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + partiallinktext + ' find timeout]')
            return False
    """
        xpath定位 
    """
    def find_element_by_xpath_ykb(self, xpath, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_xpath(xpath))
            self.log.info('--[ ' + xpath + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + xpath + ' find timeout]')
            return False

    def find_elements_by_xpath_ykb(self, xpath, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_xpath(xpath))
            self.log.info('--[ ' + xpath + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + xpath + ' find timeout]')
            return False

    """
        css定位
    """

    def find_element_by_css_ykb(self, css, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_element_by_css_selector(css))
            self.log.info('--[ ' + css + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + css + ' find timeout]')
            return False

    def find_elements_by_css_ykb(self, css, timeout=10):
        try:
            ele =  WebDriverWait(self.driver, timeout).until(lambda driver=self.driver : driver.find_elements_by_css_selector(css))
            self.log.info('--[ ' + css + ' list find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + css + ' list find timeout]')
            return False
        # 部门链接内容定位，不唯一

    """
        层级定位,应用一般是需要定位到下层的一组一样的元素
    """
    def find_element_by_hierarchy(self, method, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(method)
            self.log.info('--[ ' + 'method' + ' find ok]' )
            return ele
        except TimeoutException:
            # driver.get_screenshot_as_file("/screenshot/" + Utils.generate_time() + ".png")
            self.log.error('--[ ' + 'method' + ' find timeout]')
            return False
    """
        执行javascript脚本
        这部分的类容等具体的实际应用
    """
    # 二次封装click方法
    def click(self, ele):
        if ele is False:
            raise NoSuchElementException('查找超时，请维护脚本！')
        else:
            ele.click()
            self.log.info('--[ click ok ]')
    # 二次封装send_keys方法
    def send_keys(self,ele,value):
        if ele is False:
            raise NoSuchElementException('查找超时，请维护脚本！')
        else:
            ele.send_keys(value)
            self.log.info('--[ send_keys ok ]')
    # 等待元素消失  str_ele 定位元素的str   wait_time 每隔多长时间去扫描
    # 单据数据加载弹窗  'div[class="messager progress-bar2"]'
    # 等待老单据的提交状态中的按钮  "button[class='eui-btn eui-btn-blue btn-commit-confirm disabled']"
    def wait_element_disappear_true(self, str_ele, wait_time=0.5):
        try:
            while self.driver.find_element_by_css_selector(
                    str_ele).is_displayed() is True:
                time.sleep(wait_time)
                self.log.info('--[ wating '+ str_ele +' ]')
                print('--[ wating '+ str_ele +' ]')
        except NoSuchElementException:
            self.log.info('--[ disappear ' + str_ele + ' ]')
            print('--[ disappear ' + str_ele + ' ]')
        except StaleElementReferenceException:
            self.log.info('--[ disappear2 ' + str_ele + ' ]')
            print('--[ disappear2 ' + str_ele + ' ]')

    def wait_element_disappear_false(self, str_ele, wait_time=0.5):
        try:
            while self.driver.find_element_by_css_selector(
                    str_ele).is_displayed() is False:
                time.sleep(wait_time)
                self.log.info('--[ wating '+ str_ele +' ]')
                print('--[ wating '+ str_ele +' ]')
        except NoSuchElementException:
            self.log.info('--[ disappear ' + str_ele + ' ]')
            print('--[ disappear ' + str_ele + ' ]')
        except StaleElementReferenceException:
            self.log.info('--[ disappear2 ' + str_ele + ' ]')
            print('--[ disappear2 ' + str_ele + ' ]')

    # 元素不变，但是text变化
    def wait_element_change_by_text(self,str_ele,text_ele,wait_time=0.5):
        all_time = 0
        try:
            while text_ele in self.driver.find_element_by_css_selector(
                    str_ele).text:
                time.sleep(wait_time)
                all_time = all_time + int(wait_time)
                if all_time >= 180:
                    self.log.info('--[ 元素等待超时]')
                    return False
                self.log.info('--[ wating ' + text_ele + ' ]')
                print('--[ wating ' + text_ele + ' ]')
        except NoSuchElementException:
            self.log.info('--[ disappear ' + str_ele + ' ]')
            print('--[ disappear ' + str_ele + ' ]')
        except StaleElementReferenceException:
            self.log.info('--[ disappear2 ' + str_ele + ' ]')
            print('--[ disappear2 ' + str_ele + ' ]')

    # 判断
    # 判断JS生成的弹窗是否存在且可见
    def judge_js_pop_exist_visible(self, js_ele,wait_time=10):
        try:
            if self.find_element_by_css_ykb(js_ele,wait_time) is not False:
                return True
            else:
                return False
        except NoSuchElementException:
            self.log.info('--[ disappear ' + js_ele + ' ]')
            print('--[ disappear ' + js_ele + ' ]')
            return False
        except StaleElementReferenceException:
            self.log.info('--[ disappear2 ' + js_ele + ' ]')
            print('--[ disappear2 ' + js_ele + ' ]')
            return False

   # ----------------------------------------------------------------------------------------------
   # 以上方法基本够实际开发




































