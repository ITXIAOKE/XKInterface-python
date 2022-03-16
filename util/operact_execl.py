__author__ = "xiaoke"
import xlrd
from xlutils.copy import copy

data = xlrd.open_workbook("/Users/xiaoke/Desktop/pyProject/XKInterface-python/dataconfig/case.xls")
# 第一种拿到表
# table = data.sheet_by_name("登录")
# 第二种
# table = data.sheet_by_index(0)
# 第三种
# table=data.sheets()[0]
# 第四种
sheet_name = data.sheet_names()[0]
table = data.sheet_by_name(sheet_name)


class OperationExecl:
    '''操作execl表格的类'''

    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = "../dataconfig/case.xls"
            self.sheet_id = 0
        self.table_data = self.get_table_data()

    # 获取指定sheets的内容
    def get_table_data(self):
        data_sheet = xlrd.open_workbook(self.filename)
        table_sheet = data_sheet.sheets()[self.sheet_id]
        return table_sheet

    # 获取sheet表格的总行数
    def get_table_lines(self):
        return self.table_data.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.table_data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        '''把实际结果写入execl表格中'''
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.filename)

    # 根据列id，获取某一列的内容
    def get_col_data(self, col_id=None):
        if col_id is not None:
            col_data = self.table_data.col_values(col_id)
        else:
            col_data = self.table_data.col_values(0)
        return col_data

    # 根据行号，获取某一行的内容
    def get_row_data(self, row):
        return self.table_data.row_values(row)

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_col_data()
        for cols in cols_data:
            if case_id in cols:
                return num
            num = num + 1

    # 根据对应的caseid,找到对应的行号，进而找到对应的行内容
    def get_case_id_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_data(row_num)
        return row_data


if __name__ == '__main__':
    operate = OperationExecl()
    print(operate.get_table_lines())
    print(operate.get_cell_value(3, 4))
