import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
import ddt
import unittest
import json
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.depend_data import DependData
from util.send_mail import SendEmail
from util.operact_execl import OperationExecl
from util.operact_header import OperationHeader
from util.operact_json import OperationJson
from base.runmethod import RunMethod
import HTMLTestRunner

data = OperationExecl.get_table_data()


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = data[2]
        case_id = data[0]
        i = OperationExecl.get_table_lines(case_id)
        if is_run == 'yes':
            is_depend = data[3]
            data1 = json.loads(data[7])
            try:
                if is_depend:
                    '''
                    获取依赖数据
                    '''
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    # print(depend_data)
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]

                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie = {"is_cookie": "app"}
                if is_header == 'yes':
                    header = get_header()

                res = RunMethod.run_main(method, url, data1, cookie, get_cookie, header)
                # print(res)
                code = str(res['errorCode'])
                message = res['errorDesc']
                # message+errorcode

                if excepect_method == 'mec':
                    config_message = handle_result(url, code)
                    '''
                        if message == config_message:
                            excel_data.excel_write_data(i,13,"通过")
                        else:
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 13, "通过")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e

                if excepect_method == 'errorcode':
                    '''
                    if excepect_result == code:
                        excel_data.excel_write_data(i,14,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))
                    '''
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e
                if excepect_method == 'json':

                    if code == 1000:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    '''
                    if result:
                        excel_data.excel_write_data(i,13,"通过")
                    else:
                        excel_data.excel_write_data(i,13,"失败")
                        excel_data.excel_write_data(i,14,json.dumps(res))   
                    '''
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "失败")
                        raise e
            except Exception as e:
                excel_data.excel_write_data(i, 13, "失败")
                raise e


if __name__ == "__main__":
    case_path = base_path + "/Run"
    report_path = base_path + "/Report/report.html"
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="xiaoke", description="this is test")
        runner.run(discover)
