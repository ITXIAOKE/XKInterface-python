__author__ = "xiaoke"
import operator
import json


class CommonUtil:
    @staticmethod
    def is_contain(str_one, str_two):
        '''判断一个字符串是否在另一个字符串中'''
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    @staticmethod
    def is_equal_dict(dict_one, dict_two):
        '''判断两个字典是否相等'''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)

        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        # return cmp(dict_one, dict_two) # py2的版本,cmp函数仅仅使用字典
        # operator使用于任何对象
        return operator.eq(dict_one, dict_two)
