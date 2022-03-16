# coding=utf-8
import sys
import os

import unittest

case_path = os.getcwd() + "/case/"
print(case_path)
'''
from UnittestCase.test_case01 import TestCase01
from UnittestCase.test_case02 import TestCase02
from UnittestCase.test_case03 import TestCase03
case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
suote = unittest.TestSuite([case_01,case_02,case_03])
unittest.TextTestRunner().run(suote)
'''
discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)
# print(discover)
