__author__ = "xiaoke"


class GlobalVar:
    '''拿到execl中列的值，最后在程序的主入口中，遍历行的时候，根据行和列就能拿到cell单元格的值'''
    # id值
    ID = '0'
    # 模块
    NAME = '1'
    # 请求的url
    URL = '2'
    # 是否运行
    RUN = '3'
    # 请求的方式
    REQUEST_METHOD = '4'
    # 是否携带header
    HEADER = '5'
    # case依赖
    CASR_DEPEND = '6'
    # 依赖返回数据
    DATA_DEPEND = '7'
    # 依赖字段
    FIELD_DEPEND = '8'
    # 请求数据
    REQUEST_DATA = '9'
    # 期望结果
    EXCEPT_RESULT = '10'
    # 实际结果
    REALITY_REQUEST = '11'


def get_id():
    return GlobalVar.ID


def get_name():
    return GlobalVar.NAME


def get_url():
    return GlobalVar.URL


def get_run():
    return GlobalVar.RUN


def get_request_method():
    return GlobalVar.REQUEST_METHOD


def get_header():
    return GlobalVar.HEADER


def get_case_depend():
    return GlobalVar.CASR_DEPEND


def get_data_depend():
    return GlobalVar.DATA_DEPEND


def get_file_depend():
    return GlobalVar.FIELD_DEPEND


def get_request_data():
    return GlobalVar.REQUEST_DATA


def get_expect_result():
    return GlobalVar.EXCEPT_RESULT


def get_reality_result():
    return GlobalVar.REALITY_REQUEST
