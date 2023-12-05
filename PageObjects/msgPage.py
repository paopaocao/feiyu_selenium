#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-05 15:45
# @Author  : MSI
# @File    : msgPage.py
# @Software: PyCharm
import time

from selenium.webdriver import ActionChains, Keys

from utils import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class MsgPage:
    def __init__(self, driver: webdriver, selector_data: dict):
        self.driver = driver
        self.selector_data = selector_data

    def Fix_bug(self):
        """
        23333 不解决bug无法聊天
        :return:
        """
        # 等待通讯录加载
        address_box = self.selector_data["msg_page"]["nav"]["address_box"]
        address_box_method = search_element_by(selector_method(address_box))
        address_box_element = selector_element(address_box, selector_method(address_box))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, address_box_element))
        )
        # 默认在聊天nav，先点击一次审核，不然无法进入私人聊天，奇怪的bug..
        feed = self.selector_data["msg_page"]["slider"]["feed"]
        feed_method = search_element_by(selector_method(feed))
        feed_element = selector_element(feed, selector_method(feed))
        WebDriverWait(self.driver, 5).until(lambda p: p.find_element(feed_method, feed_element))
        listNav = self.driver.find_element(feed_method, feed_element)

        # 查找审批。这个系统号是肯定能进去私聊的
        user_msg_items = self.selector_data["msg_page"]["user_msg_items"]
        user_msg_items_method = search_element_by(selector_method(user_msg_items))
        user_msg_items_element = selector_element(user_msg_items, selector_method(user_msg_items))

        user_item = self.selector_data["msg_page"]["slider"]["user_item"]
        user_item_method = search_element_by(selector_method(user_item))
        user_item_element = selector_element(user_item, selector_method(user_item))

        message_list = listNav.find_element(user_msg_items_method, user_msg_items_element).find_elements(
            user_item_method,
            user_item_element)

        for message in message_list:
            # 每个用户
            if message.get_attribute("aria-label") == "审批":
                message.click()
                return True
        return False

    def move_to_external_contacts(self):
        # 整个聊天背景
        layout_content = self.selector_data["msg_page"]["layout_content"]
        layout_content_method = search_element_by(selector_method(layout_content))
        layout_content_element = selector_element(layout_content, selector_method(layout_content))
        # 外部联系人
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, layout_content_element))
        )
        # 点击通讯录
        address_box = self.selector_data["msg_page"]["nav"]["address_box"]
        address_box_method = search_element_by(selector_method(address_box))
        address_box_element = selector_element(address_box, selector_method(address_box))
        self.driver.find_element(address_box_method, address_box_element).click()

        ext_contacts = self.selector_data["msg_page"]["address"]["ext_contacts"]
        ext_contacts_method = search_element_by(selector_method(ext_contacts))
        ext_contacts_element = selector_element(ext_contacts, selector_method(ext_contacts))
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, ext_contacts_element))
        )
        time.sleep(3)
        # 点击外部联系人
        self.driver.find_element(ext_contacts_method, ext_contacts_element).click()
        time.sleep(3)
        # 用户合集
        user_msg_items = self.selector_data["msg_page"]["user_msg_items"]
        user_msg_items_method = search_element_by(selector_method(user_msg_items))
        user_msg_items_element = selector_element(user_msg_items, selector_method(user_msg_items))
        user_list = self.driver.find_elements(user_msg_items_method, user_msg_items_element)

        for user in user_list:
            user_name = self.selector_data["msg_page"]["address"]["user_name"]
            user_name_method = search_element_by(selector_method(user_name))
            user_name_element = selector_element(user_name, selector_method(user_name))
            user = user.find_element(user_name_method, user_name_element)

            friend_name = self.selector_data["msg_page"]["friend_name"]
            if user.text == friend_name:
                user.click()
                send_msg = self.selector_data["msg_page"]["address"]["send_msg"]
                send_msg_method = search_element_by(selector_method(send_msg))
                send_msg_element = selector_element(send_msg, selector_method(send_msg))
                WebDriverWait(self.driver, 5).until(lambda p: p.find_element(send_msg_method, send_msg_element))
                self.driver.find_element(send_msg_method, send_msg_element).click()
                break

        # 等待 chatSidebar
        chat_sidebar = self.selector_data["msg_page"]["chat_sidebar"]
        chat_sidebar_method = search_element_by(selector_method(chat_sidebar))
        chat_sidebar_element = selector_element(chat_sidebar, selector_method(chat_sidebar))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, chat_sidebar_element))
        )
        # 输入文本发送
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(chat_sidebar_method, chat_sidebar_element)).pause(
            3) \
            .send_keys(self.selector_data["msg_page"]["send_test_msg"]).key_down(Keys.ENTER).perform()

        print("发送成功")
