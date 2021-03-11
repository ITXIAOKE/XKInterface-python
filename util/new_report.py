__author__ = "xiaoke"
import os

file_path = "E:\\pycharmProject\\interface\\interfaceMyProject\\reports\\interface"
lists = os.listdir(file_path)
print(lists)
# 重新按时间对目录下的报告进行排序
lists.sort(key=lambda fn: os.path.getmtime(file_path + "\\" + fn))
# 最新的文件
print(lists[-1])
file = os.path.join(file_path, lists[-1])
print(file)
