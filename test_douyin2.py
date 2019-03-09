# -*- coding:utf-8 -*-

# server 启动参数
import time

def video_url_download():
    from appium import webdriver
    # v = open('video.txt','a+')
    # v_list = v.read().split()
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1'
    desired_caps['deviceName'] = '721QADRG227LK'
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

    # time.sleep(20)
    print('start')
    time.sleep(10)
    # 向上滑动屏幕
    for i in range(10):
        # print(sc_size)
        x = sc_size.get('width')
        y = sc_size.get('height')
        driver.swipe(x*0.5,y*0.8,x*0.5,y*0.2)
        # print(driver.page_source)
        time.sleep(0.5)

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
    # n = 0
    # for url in video_list:
    #     m.update(url.encode())
    #     vname = m.hexdigest()
    #     if vname not in v_list:
    #         print(url)
    #         host_url = url.split('/video')[0]
    #         headers.update({"Host":host_url})
    #         v.write(vname + '\n')
    #         with open('Video/%s.mp4' % vname,'wb') as f:
    #             res = requests.get(url)
    #             content_size = int(res.headers['content-length'])
    #             print(content_size)
    #             print('[文件大小]：%0.2f MB' % (content_size/1024/1024))
    #             if content_size == 169:
    #                 print("403 forbidden")
    #                 continue
    #             f.write(res.content)
    #         n += 1
    # print("共%s个视频" % n)

