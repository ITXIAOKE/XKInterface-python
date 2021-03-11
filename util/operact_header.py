__author__ = "xiaoke"
import requests
import json
from util.operact_json import OperationJson


class OperationHeader:
    '''操作header 中cookie的类'''

    def __init__(self, response):
        self.operate_json = OperationJson()
        self.response = json.loads(response)

    def get_response_url(self):
        '''获取登录返回token中的url'''
        return self.response['data']['url'][0]

    def get_cookie(self):
        '''获取cookie的jar文件'''
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        '''写字典类型的cookie信息到json文件中'''
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        self.operate_json.write_data(cookie)
