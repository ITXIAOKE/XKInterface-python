# coding=utf-8
# selenium web
import requests
import json
import time
from selenium import webdriver

cookie1 = {
    "apsid": ""
}
driver = webdriver.Chrome()
driver.get("https://www.imooc.com/user/newlogin")
time.sleep(4)
# driver.find_element_by_id("js-signin-btn").click()
time.sleep(3)
driver.find_element_by_name("email").send_keys("xiaoke@163.com")
driver.find_element_by_name("password").send_keys("x134168")
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(3)
cookie = driver.get_cookies()
for i in cookie:
    if i['name'] == 'apsid':
        cookie1['apsid'] = i['value']
print(cookie1)
driver.close()

download_url = 'https://www.imooc.com/user/postpic'
file = {
    "fileField": ("test.jpg", open("../test.jpg", "rb"), "image/jpg"),
    "type": "1"
}
res = requests.post(url=download_url, files=file, cookies=cookie1, verify=False).text
print(res)
