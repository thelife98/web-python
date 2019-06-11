#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
如果项目不需要使用utx，在调试单个用例的时候，需要先调用utx.stop_patch()，暂停utx对unittest模块的注入
"""

import utx
utx.stop_patch()  # 如果注释掉这句，运行会报错

from testsuite.testcase1.test_bls_tems_declare import TestMachinList
import unittest

if __name__ == "__main__":
    '''
    if 想用来调试某个测试类中的某个类方法，
    比如这里是调试testcase1文件夹中的测试类TestMachinList中的类方法test_login_user，
    请使用以下这四句代码
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestMachinList("test_login_user"))
    runner=unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

    '''
    else 想调试某个测试类，
    比如这里是调试testcase1文件夹中的测试类TestMachinList，
    请使用以下这四句代码
    '''
    # test_dir='./testcase1'
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_bls_tems_declare.py')
    # runner=unittest.TextTestRunner(verbosity=3)
    # runner.run(discover)