# -*- coding:utf-8 -*-

# server 启动参数
import time

from appium import webdriver

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = '882QAETHJ6LSW '
# 指定appium框架版本
# desired_caps['automationName'] = 'Uiautomator2'
# 设置中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app的信息
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = '.main.MainActivity'
# 会话不重置
desired_caps['noReset'] = True
# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)
sc_size = driver.get_window_size()

time.sleep(5)
# 向上滑动屏幕
# while True:
for i in range(100):
    # print(sc_size)
    x = sc_size.get('width')
    y = sc_size.get('height')
    driver.swipe(x*0.5,y*0.8,x*0.5,y*0.2)
    # print(driver.page_source)
    time.sleep(15)

# # 点击搜索
# driver.find_element_by_id("com.ss.android.ugc.aweme:id/aci").click()
# # 点击搜索框，清空并输入绮里小爱搜索
# search_input = driver.find_element_by_class_name("android.widget.EditText")
# search_input.click()
# search_input.clear()
# search_input.send_keys('绮里小爱')
# driver.find_element_by_xpath("//*[contains(@text,'搜索')]").click()
time.sleep(5)
driver.quit()

# from hashlib import md5
# m = md5()
# from s_url import diguimulu
# import requests
#
# video_list = diguimulu('douyin')
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#
# for url in video_list:
#     m.update(url.encode())
#     print(url)
#     with open('Video/%s.mp4' % m.hexdigest(),'wb') as f:
#         res = requests.get(url)
#         f.write(res.content)