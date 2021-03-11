__author__ = "xiaoke"
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.depend_data import DependData
from util.send_mail import SendEmail
from util.operact_header import OperationHeader
from util.operact_json import OperationJson
# from base import HTMLTestRunner
# import HtmlTestRunner
import HTMLTestRunner
import unittest


class TestRun(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    # 整个项目执行的主入口
    def test_go_on_run(self):
        pass_count = []
        fail_count = []
        # 这个表格所有的行数，也就是所有的接口数
        rows_count = self.data.get_case_lines()
        # 一行一行的执行所有的接口
        for i in range(1, rows_count):
            # 判断该接口是否运行
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_from_json(i)
                header = self.data.is_header(i)
                # 从表格中拿期望的值
                expect = self.data.get_expect_data(i)
                # 从数据库中拿期望的值
                # expect_db = self.data.get_expcet_data_for_mysql(i)
                # 获取该条case是否有依赖case
                depend_case = self.data.is_depend(i)
                if depend_case is not None:
                    # 把拿到的依赖case传给依赖case操作的类
                    depend_data = DependData(depend_case)
                    # 获取依赖返回数据
                    depend_response_data = depend_data.get_data_for_key(i)
                    # 获取依赖字段
                    depend_field = self.data.get_depend_field(i)
                    # 更改请求数据中依赖的字段值
                    request_data[depend_field] = depend_response_data

                # 发送真正的请求
                # res = self.run_method.run_main(method, url, request_data, header)
                # print(res)
                # 第一次开启要写登录的token，第二次要拿登录token信息，其他的接口则不需要这种token信息
                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    operate_header = OperationHeader(res)
                    operate_header.write_cookie()
                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {
                        'apsid': cookie
                    }
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                # 判断期望的值是否在返回的数据中
                if self.com_util.is_contain(expect, res):
                    # 注意这里操作execl的时候，一定要关闭execl，否则报操作execl权限失败的问题
                    self.data.write_result(i, "pass")
                    pass_count.append(i)
                    self.assertIn(expect, res)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
                    self.assertNotIn(expect, res)
        # 统计成功的接口数和失败的接口数，发送邮件
        # self.send_mail.send_main(pass_count, fail_count)
        # self.send_mail.send_mail_fujian()
        # self.send_mail.send_mail_fujian_new_report()
        print(pass_count)
        print(fail_count)

    @classmethod
    def tearDownClass(cls):
        file_name = SendEmail().new_report()
        SendEmail().send_mail_fujian_new_report(file_name)


if __name__ == '__main__':
    # go = TestRun()
    # go.test_go_on_run()
    unittest.main(testRunner=HTMLTestRunner(stream="interface",verbosity=1))
