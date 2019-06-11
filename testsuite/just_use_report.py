#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
单独使用测试报告组件，不需要utx的功能，也就不能按照测试案例顺序执行，而是按照unittest执行规则0-9，A-Z，a-z
"""
import utx

if __name__ == '__main__':
    utx.stop_patch() # 如果注释掉这句，运行会报错
    runner = utx.TestRunner()
    runner.add_case_dir(r"testcase1") #添加测试用例文件夹，多次调用可以添加多个文件夹，会按照文件夹的添加顺序执行用例
    runner.run_test(report_title='接口自动化测试报告')