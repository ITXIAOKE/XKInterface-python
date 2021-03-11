__author__ = "xiaoke"
import json
import requests


class RunMethod:

    def post_main(self, url, data, header=None):
        # 注意这里要判断表格中是否携带header是一个字符串no
        if header != "no" and header is not None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        if header != "no" and header is not None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        if method == "Post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        # 没有格式化的字典，在拿期望值的时候做处理了，所以用以下的方式
        # return json.dumps(res, ensure_ascii=False)
        # 格式化的字典，方便好看，但是不能作为两个字典比较
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
