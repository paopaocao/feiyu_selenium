#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023-12-05 15:46
# @Author  : MSI
# @File    : utils.py
# @Software: PyCharm
import yaml
from selenium.webdriver.common.by import By


def search_element_by(by: str) -> By:
    if by == "class":
        return By.CLASS_NAME
    else:
        return By.CSS_SELECTOR


def selector_dict() -> dict:
    with open("selector_data.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data


def selector_method(method_dict: dict) -> str:
    return list(method_dict.keys())[0]


def selector_element(method_dict: dict, method: str):
    return method_dict[method]


if __name__ == '__main__':
    print(selector_method(selector_dict()['home_page']['mask']['popup']))
