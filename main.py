#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-05 15:40
# @Author  : MSI
# @File    : version2.py
# @Software: PyCharm

import time
from selenium import webdriver
from PageObjects import *
from utils import *

if __name__ == '__main__':
    webdriver = webdriver.Chrome()
    selector_data = selector_dict()

    # 实例化PageObj
    home = HomePage(webdriver, selector_data)
    login = LoginPage(webdriver, selector_data)
    msg = MsgPage(webdriver, selector_data)

    # 进入首页
    home.open_browser()
    # 关闭遮罩
    home.close_mask()
    # 进入登录
    home.move_to_login()
    # 登陆
    login.login()
    # 等待5秒
    time.sleep(5)
    # 打开首页信息
    home.move_to_msg()
    # 进入聊天框 ...解决bug
    msg.Fix_bug()
    # 进入外部联系人，发送消息
    msg.move_to_external_contacts()

    time.sleep(50)
    webdriver.quit()
