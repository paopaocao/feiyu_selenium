#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-05 15:45
# @Author  : MSI
# @File    : loginPage.py
# @Software: PyCharm
from utils import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class LoginPage:
    def __init__(self, driver: webdriver, selector_data: dict):
        self.driver = driver
        self.selector_data = selector_data

    def login(self):
        wait_page = self.selector_data["login_page"]["wait_page"]
        wait_page_method = search_element_by(selector_method(wait_page))
        wait_page_element = selector_element(wait_page, selector_method(wait_page))
        WebDriverWait(self.driver, 5).until(lambda p: p.find_element(wait_page_method, wait_page_element))
        # 小电脑
        to_mobile_login = self.selector_data["login_page"]["to_mobile_login"]
        to_mobile_login_method = search_element_by(selector_method(to_mobile_login))
        to_mobile_login_element = selector_element(to_mobile_login, selector_method(to_mobile_login))
        self.driver.find_element(to_mobile_login_method, to_mobile_login_element).click()

        # 输入手机号
        input_mobile = self.selector_data["login_page"]["input_mobile"]
        input_mobile_method = search_element_by(selector_method(input_mobile))
        input_mobile_element = selector_element(input_mobile, selector_method(input_mobile))
        self.driver.find_element(input_mobile_method, input_mobile_element) \
            .send_keys(self.selector_data["user"]["user_mobile"])

        # 同意服务
        check_policy = self.selector_data["login_page"]["check_policy"]
        check_policy_method = search_element_by(selector_method(check_policy))
        check_policy_element = selector_element(check_policy, selector_method(check_policy))
        self.driver.find_element(check_policy_method, check_policy_element).click()

        # 下一步
        next_to_password = self.selector_data["login_page"]["next_to_password"]
        next_to_password_method = search_element_by(selector_method(next_to_password))
        next_to_password_element = selector_element(next_to_password, selector_method(next_to_password))
        self.driver.find_element(next_to_password_method, next_to_password_element).click()
        try:
            input_password = self.selector_data["login_page"]["input_password"]
            input_password_method = search_element_by(selector_method(input_password))
            input_password_element = selector_element(input_password, selector_method(input_password))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, input_password_element))
            )
            # 登陆
            self.driver.find_element(input_password_method, input_password_element) \
                .send_keys(self.selector_data["user"]["user_password"])
            # 下一步
            login_button = self.selector_data["login_page"]["login_button"]
            login_button_method = search_element_by(selector_method(login_button))
            login_button_element = selector_element(login_button, selector_method(login_button))
            self.driver.find_element(login_button_method, login_button_element).click()

        except TimeoutException:
            print("等待元素出现超时")
            return False
        else:
            return True
        finally:
            return False
