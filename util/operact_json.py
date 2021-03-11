__author__ = "xiaoke"
import json


class OperationJson:
    '''操作json的类'''

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path

        self.json_data = self.get_json_data()
        # print(self.json_data)

    # 获取指定的json文件
    def get_json_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
            return data

    # 在生成的json字典中根据指定的键获取指定的值
    def get_data(self, name):
        return self.json_data[name]

    # 写json，例如把登录时候的cookie写入到这个json文件中
    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'wb') as fp:
            # 把字典类型的cookie信息转化为字符串，保存起来
            fp.write(json.dumps(data))


if __name__ == '__main__':
    json = OperationJson()
    print(json.get_data("user"))
