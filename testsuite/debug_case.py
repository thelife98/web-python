#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
使用utx，调试带有数据驱动的单个用例，不生成报告
"""
import utx
from testsuite.testcase1.test_bls_tems_declare import TestMachinList

utx.run_case(TestMachinList,"test_login_user")

