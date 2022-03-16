# coding=utf-8
import sys
import os

base_path = os.getcwd()
import unittest

sys.path.append(base_path)
import unittest
from base.runmethod import RunMethod

url = "http://www.imooc.com"
data = {
    "username": "1111",
    "password": "22222"
}
host = 'http://www.imooc.com'


class TestCase01(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case结束执行")

    @classmethod
    def setUpClass(cls):
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skip("这个case不想执行")
    def test_07(self):
        print("执行case07")
        flag = "adfadfadfadfadsfaqeewr"
        s = "fads"
        self.assertIn(s, flag, msg="不包含")

    @unittest.skip("这个case不想执行")
    def test_01(self):
        TestCase01.a = 5
        print("执行case01")
        # res = requests.get(url=url,params=data).json()
        data1 = {
            "user": "11111"
        }
        self.assertDictEqual(data1, data)

    @unittest.skip("这个case不像执行")
    def test_02(self):
        print("----------------》执行case02")
        data1 = {
            "username": "1111",
            "password": "22222"
        }
        self.assertDictEqual(data1, data, msg="这两个字典不相等")

    @unittest.skip("这个case不像执行")
    def test_03(self):
        print("执行case03")
        flag = True
        self.assertFalse(flag, msg="不等于True")

    @unittest.skip("这个case不想执行")
    def test_04(self):
        print("执行case04")
        flag = False
        self.assertTrue(flag, msg="不等于False")

    @unittest.skipIf(host != "http://www.imooc.com", "这个case不执行")
    def test_05(self):
        print("执行case05")
        flag = "111"
        flag1 = "2222"
        self.assertEqual(flag, flag1, msg="两个str不相等")

    def test_06(self):
        res = RunMethod.run_main("get", url, data)
        print(res)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    '''
    suite.addTest(TestCase01('test_06'))
    suite.addTest(TestCase01('test_04'))
    suite.addTest(TestCase01('test_02'))
    suite.addTest(TestCase01('test_05'))
    suite.addTest(TestCase01('test_01'))
    suite.addTest(TestCase01('test_07'))
    '''
    tests = [TestCase01('test_06'), TestCase01('test_02'), TestCase01('test_03'), TestCase01('test_05'),
             TestCase01('test_01')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
