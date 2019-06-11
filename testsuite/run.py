#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""完整使用utx功能的demo"""

from utx import *
import logging

if __name__ == '__main__':
    setting.run_case = {Tag.ALL}  # 运行全部测试用例
    # setting.run_case = {Tag.SMOKE}  # 只运行SMOKE标记的测试用例
    # setting.run_case = {Tag.SMOKE, Tag.V8_3_7}   # 只运行SMOKE和V8_3_7标记的测试用例

    setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
    setting.full_case_name = True #显示完整用例名字（函数名字+参数信息）
    setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
    setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
    setting.sort_case = True  # 是否按照编写顺序，对用例进行排序

    """可选择使用样式1或样式2的报告模板"""
    setting.create_report_by_style_1 = True  # 测试报告样式1
    setting.create_report_by_style_2 = True  # 测试报告样式2

    log.set_level(logging.DEBUG)  # 设置utx的log级别
    # log.set_level_to_debug()     # 设置log级别的另外一种方法，与上面这句的效果一样

    runner = TestRunner()
    runner.add_case_dir(r"testcase1") #添加测试用例文件夹，多次调用可以添加多个文件夹，会按照文件夹的添加顺序执行用例
    runner.run_test(report_title='接口自动化测试报告')
