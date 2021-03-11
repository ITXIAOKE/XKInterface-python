import requests

# res = requests.get("http://www.baidu.com")
# print(res.status_code)
# print(res.encoding)
# # print(res.text)
# if isinstance(res.text, ()):
#     print("True")
# else:
#     print("Flase")


# def num():
#     return [lambda x: i * x for i in range(4)]
#
# print(num())
# a = [m(2) for m in num()]
# print(a)

# coding=utf-8 
def originalFunc():
    print('this is original function!')

def modifiedFunc():
    modifiedFunc = 1
    print('this is modified function!')

def main():
    originalFunc()

if __name__ == '__main__':
    originalFunc = modifiedFunc  # 这句是加的猴子补丁
    main()