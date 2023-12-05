#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-05 15:45
# @Author  : MSI
# @File    : homePage.py
# @Software: PyCharm
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from utils import *


class HomePage:
    def __init__(self, driver: webdriver, selector_data: dict):
        self.driver = driver
        self.selector_data = selector_data

    def open_browser(self):
        self.driver.get(self.selector_data["base_url"])
        WebDriverWait(self.driver, 5).until(lambda p: p.find_element(By.CLASS_NAME, "ftHeader-bar"))

    def close_mask(self):
        try:
            popup = self.selector_data["home_page"]["mask"]["popup"]
            popup_method = search_element_by(selector_method(popup))
            popup_element = selector_element(popup, selector_method(popup))
            mask = self.driver.find_element(popup_method, popup_element)

            mask_close = self.selector_data["home_page"]["mask"]["mask_close"]
            mask_close_method = search_element_by(selector_method(mask_close))
            mask_close_element = selector_element(mask_close, selector_method(mask_close))
            mask.find_element(mask_close_method, mask_close_element).click()
            print("关闭遮罩Success")
            return True
        except NoSuchElementException:
            print("元素不存在")
            return False

    def move_to_login(self):
        login_button = self.selector_data["home_page"]["to_login"]["button"]
        login_button_method = search_element_by(selector_method(login_button))
        login_button_element = selector_element(login_button, selector_method(login_button))
        self.driver.find_element(login_button_method, login_button_element).click()

        isJumpToLogin = "login.feishu.cn" in self.driver.current_url
        if isJumpToLogin:
            return True
        else:
            return False

    def move_to_msg(self):
        container_list = self.selector_data["home_page"]["to_msg"]["container_list"]
        container_list_method = search_element_by(selector_method(container_list))
        container_list_element = selector_element(container_list, selector_method(container_list))
        self.driver.find_element(container_list_method, container_list_element).click()

        current_windows = len(self.driver.window_handles)
        # 进入聊天框
        grid_list = self.selector_data["home_page"]["to_msg"]["grid_list"]
        grid_list_method = search_element_by(selector_method(grid_list))
        grid_list_element = selector_element(grid_list, selector_method(grid_list))
        ulList = self.driver.find_element(grid_list_method, grid_list_element)

        ulList.find_elements(By.CSS_SELECTOR, "ul > li")[0].click()
        # switch聊天窗口
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > current_windows)
        for window_handle in self.driver.window_handles:
            if window_handle != self.driver.current_window_handle:
                self.driver.switch_to.window(window_handle)
                return True
        return False
