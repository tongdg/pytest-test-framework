#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2019-07-08 Created by tongdg'

from pages.base_page import BasePage
import time
from selenium import webdriver


class BusinessTravelPage(BasePage):

    """
        页面元素：
        机票：
        选择出发日期->查询机票按钮->等待loding加载完->显示所有航班->选择第一个航班->预定->等待loding加载完->提交审批
        ->判断是否有错->有错（如果身份证错误）->修改身份证->点击修改->输入身份证->确定->提交审批->等待loading加载完
        酒店：
        点击目的地->输入地址->点击下拉框->点击入住时间->选择入住时间->点击离店时间->选择离店时间->点击搜索->等待loding->
        选择第一家酒店->点击第一个房型->点击提交订单->等待loding加载完

    """
    # 出发日期
    @property
    def flight_departture_date(self):
        return self.find_element_by_class_name_ykb('setOutDay')

    # 时间控件,获取所有的有效的天数，
    @property
    def time_contro_day(self):
        return self.find_elements_by_css_ykb("td[class='day']")

    # 查询机票按钮
    @property
    def query_plane_ticket_btn(self):
        return self.find_element_by_class_name_ykb('searchTicket')

    # 显示所有航班按钮
    @property
    def display_all_flight(self):
        return self.find_elements_by_class_name_ykb('uncomp_fligt')

    # 选择第一个航班信息
    @property
    def choose_first_flight_info(self):
        return self.find_elements_by_class_name_ykb('select_btn')

    # 预定第一个
    @property
    def reserve_first(self):
        return self.find_elements_by_class_name_ykb('choice_this')

    # 提交审批
    @property
    def submit_to_approval(self):
        return self.find_element_by_class_name_ykb('btnSub')

    # 错误消息提示框
    @property
    def messager_error(self):
        return self.find_element_by_css_ykb("div[class='messager error']")

    # 修改身份证按钮
    @property
    def modify_ID_btn(self):
        return self.find_element_by_class_name_ykb('preserved')

    # 输入正确的身份证
    @property
    def input_right_ID(self):
        return self.find_element_by_id_ykb('editIdno')

    # 确定按钮
    @property
    def ID_confirm_btn(self):
        return self.find_element_by_css_ykb('#editModal > div > div > div.confirmnew-modal-footer > button.eui-btn.eui-btn-blue.btn-modal-confirm',50)

    # flight_iframe
    @property
    def get_flight_iframe(self):
        return self.find_elements_by_class_name_ykb("flight-query")

    # 手机号输入
    @property
    def input_phone_number(self):
        return self.find_element_by_class_name_ykb('link_cell')

    # 目的地
    @property
    def from_city(self):
        return self.find_element_by_id_ykb('fromCity')

    # 选择上海
    @property
    def choose_shanghai(self):
        return self.find_element_by_link_text_ykb('上海')

    # 入住
    @property
    def check_in_time(self):
        return self.find_element_by_id_ykb('checkInDate')

    # 离店
    @property
    def check_out_time(self):
        return self.find_element_by_id_ykb('checkOutDate')

    # 搜索按钮
    @property
    def hotel_query_btn(self):
        return self.find_element_by_id_ykb('start-search')

    # 酒店列表
    @property
    def hotel_list(self):
        return self.find_elements_by_class_name_ykb('hotel-list')

    # 房型
    @property
    def hotel_house(self):
        return self.find_elements_by_class_name_ykb('roomContentList')

    # 酒店支付方式
    @property
    def hotel_pay_way(self):
        return self.find_elements_by_class_name_ykb('payMethod')

    # 酒店订单提交
    @property
    def hotel_order_submit(self):
        return self.find_element_by_class_name_ykb('subscribe')

    # 选择酒店
    def choose_hotel(self):
        time.sleep(1)
        self.driver.switch_to.frame(self.get_flight_iframe[0])
        time.sleep(3)
        self.click(self.from_city)
        time.sleep(1)
        self.click(self.choose_shanghai)
        time.sleep(1)
        self.click(self.check_in_time)
        time.sleep(1)
        self.click(self.time_contro_day[1])
        time.sleep(1)
        self.click(self.check_out_time)
        time.sleep(1)
        self.click(self.time_contro_day[3])
        time.sleep(1)
        self.click(self.hotel_query_btn)
        self.wait_element_disappear_false("body > div.loading-modal")
        self.click(self.hotel_list[0])
        self.wait_element_disappear_true("body > div.loading-modal")
        hh = self.hotel_house
        temp = 0
        for hl in hh:
            self.click(hl)
            types = self.find_element_by_hierarchy(
                lambda var : hl.find_elements_by_class_name('payUnify')
            )
            for typ in types:
                if typ.text == '公司统付':
                    self.click(typ)
                    self.wait_element_disappear_false("body > div.loading-modal")
                    print('点击ok')
                    temp = 1
                    break
            if temp == 1:
                break
        time.sleep(1)
        self.click(self.hotel_order_submit)
        self.wait_element_disappear_true("body > div.loading-modal")
        self.wait_element_disappear_true('#e7ticket_modalbox_bta_hotel_ticket_booking_btn > div')
        self.driver.switch_to.default_content()

    # 选择机票
    def choose_flight(self):
        time.sleep(1)
        self.driver.switch_to.frame(self.get_flight_iframe[0])
        # 等待页面的加载
        time.sleep(2)
        self.click(self.flight_departture_date)
        time.sleep(1)
        self.click(self.time_contro_day[1])
        time.sleep(1)
        self.click(self.query_plane_ticket_btn)
        self.wait_element_disappear_true("div[class='beforeContent']")
        self.click(self.display_all_flight[1])
        time.sleep(1)
        self.click(self.choose_first_flight_info[0])
        time.sleep(1)
        self.click(self.reserve_first[0])
        time.sleep(1)
        self.click(self.modify_ID_btn)
        time.sleep(1)
        self.send_keys(self.input_right_ID,'513701199512016339')
        time.sleep(1)
        self.click(self.ID_confirm_btn)
        time.sleep(1)
        self.input_phone_number.clear()
        time.sleep(1)
        self.send_keys(self.input_phone_number,'15216625816')
        time.sleep(1)
        self.click(self.submit_to_approval)
        self.wait_element_disappear_true("div[class='beforeContent']")
        self.wait_element_disappear_true('#e7ticket_modalbox_bta_hotel_ticket_booking_btn > div')
        # self.driver.switch_to.default_content()


























