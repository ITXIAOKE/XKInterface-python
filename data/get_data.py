__author__ = "xiaoke"

from util.operact_execl import OperationExecl
from util.operact_json import OperationJson
from data import data_config


# 操作execl，拿到execl中所有的数据
class GetData:
    def __init__(self):
        self.operation_execl = OperationExecl()
        self.operation_json = OperationJson()

    # 获取execl中行数，也就是我们的case个数
    def get_case_lines(self):
        return self.operation_execl.get_table_lines()

    # 获取是否执行
    def get_is_run(self, row):
        col = int(data_config.get_run())
        run_model = self.operation_execl.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header,如果携带header就把对应的header 判断yes或者no拿到
    def is_header(self, row):
        col = int(data_config.get_header())  # 列
        header = self.operation_execl.get_cell_value(row, col)
        if header != "":
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_method())
        request_method = self.operation_execl.get_cell_value(row, col)
        if request_method == "":
            return None
        else:
            return request_method

    # 获取请求的url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.operation_execl.get_cell_value(row, col)
        if url == "":
            return None
        else:
            return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_request_data())
        data = self.operation_execl.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

    # 通过获取关键字拿到data数据
    def get_data_from_json(self, row):
        data_name = self.get_request_data(row)
        request_data = self.operation_json.get_data(data_name)
        if request_data == "":
            return None
        else:
            return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect_result())
        expect_value = self.operation_execl.get_cell_value(row, col)
        if expect_value == "":
            return None
        else:
            return expect_value

    # 把实际结果值写入execl中
    def write_result(self, row, value):
        col = int(data_config.get_reality_result())
        self.operation_execl.write_value(row, col, value)

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.operation_execl.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取依赖返回数据的key,根据这个key可以从文件中找到对应的值
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depend_key = self.operation_execl.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_file_depend())
        field_depend = self.operation_execl.get_cell_value(row, col)
        if field_depend == "":
            return None
        else:
            return field_depend

    # 通过sql获取预期结果
    def get_expcet_data_for_mysql(self, row):
        from util.operact_mysql import OperationMysql
        op_mysql = OperationMysql()
        # 获取表格中的sql语句
        sql = self.get_expect_data(row)
        # 通过一条sql查询出一条数据
        res = op_mysql.search_one(sql)
        return res
