__author__ = "xiaoke"

import json
import sys
from jsonpath_rw import jsonpath, parse
from util.operact_execl import OperationExecl
from data.get_data import GetData
from base.runmethod import RunMethod
from util.operact_json import OperationJson


class DependData:
    '''数据依赖操作的类'''

    def __init__(self, case_id):
        self.operate_execl = OperationExecl()
        self.get_data = GetData()
        self.run_method = RunMethod()
        self.case_id = case_id

    # 通过caseid去获取该caseid的整行数据
    def get_case_line_data(self):
        return self.operate_execl.get_case_id_row_data(self.case_id)

    # 执行依赖测试获取结果
    def run_dependent(self):
        row_num = self.operate_execl.get_row_num(self.case_id)
        request_data = self.get_data.get_data_from_json(row_num)

        method = self.get_data.get_request_method(row_num)
        url = self.get_data.get_request_url(row_num)

        # 注意这里的header再执行依赖测试的时候也需要再判断一下,因为依赖的测试接口可能没有携带header
        header = self.get_data.is_header(row_num)
        # if header == "yes":
        #     op_json = OperationJson('../dataconfig/cookie.json')
        #     cookie = op_json.get_data('apsid')
        #     cookies = {
        #         'apsid': cookie
        #     }
        #     res = self.run_method.run_main(method, url, request_data, cookies)
        # elif header == "no":
        #     res = self.run_method.run_main(method, url, request_data)

        res = self.run_method.run_main(method, url, request_data, header)
        # 这里由于请求的数据中buy和shop接口每次不一样，我文件user.json中数据是很久前的，那么就会导致服务器没有返回数据
        # print(res)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应数据，然后返回
    def get_data_for_key(self, row):
        depend_data = self.get_data.get_depend_key(row)
        response_data = self.run_dependent()
        # 有jsonpath_rw来一层一层的找数据，先建立这个匹配规则
        json_exe = parse(depend_data)
        # 根据匹配规则去数据中查找是否有这样匹配规则的数据
        madle = json_exe.find(response_data)
        # 返回的数据为空，那么madle列表中的数据为空
        if len(madle) > 0:
            return [math.value for math in madle][0]
        else:
            return None


if __name__ == '__main__':
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.out_trade_no"
    json_exe = parse(res)
    print(json_exe)
    madle = json_exe.find(order)
    print(madle)
    print([math.value for math in madle][0])
