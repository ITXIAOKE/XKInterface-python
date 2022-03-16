import sys
import os

from util.operact_execl import OperationExecl
# base_path = os.getcwd()
# sys.path.append(base_path)

import ddt
import unittest

operate = OperationExecl()
data = operate.get_table_data()


# data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]

@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    @ddt.data(*data)
    def test_01(self, data1):
        # case编号	作用	是否执行	前置条件	依赖key	url	method	data	cookie操作	header操作	预期结果方式	预期结果	result	数据
        function, is_run, depend_key, url, method, request_data, cookie, header, execpet_method, execpet, result, result_data = data

        print("this is test case", function, is_run, depend_key, url, method, request_data, cookie, header,
              execpet_method, execpet, result, result_data)


if __name__ == "__main__":
    unittest.main()
