# -*- coding:utf-8 -*-

# server 启动参数
import os
import time
import shutil
from appium import webdriver


def video_url_download():
    shutil.rmtree("douyin")
    os.mkdir("douyin")
    # v = open('video.txt','a+')
    # v_list = v.read().split()
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = '882QAETHJ6LSW'
    # 指定appium框架版本
    desired_caps['automationName'] = 'Uiautomator2'
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
    # time.sleep(10)
    # 点击进入搜索
    try:
        # driver.find_element_by_id("com.ss.android.ugc.aweme:id/am1").click()
        # driver.find_element_by_id("com.ss.android.ugc.aweme:id/ao6").click()
        # 8.1
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/amy").click()
    except Exception as e:
        print(e)
        driver.quit()
    # 搜索框输入名字
    name = input("请输入要下载的视频作者名字：")
    # search_box = driver.find_element_by_id("com.ss.android.ugc.aweme:id/acx")
    # search_box = driver.find_element_by_id("com.ss.android.ugc.aweme:id/af2")
    # 8.1
    search_box = driver.find_element_by_id("com.ss.android.ugc.aweme:id/adr")

    search_box.click()
    search_box.send_keys(name)
    # 点击搜索获取搜索结果
    # driver.find_element_by_id("com.ss.android.ugc.aweme:id/ad0").click()
    # driver.find_element_by_id("com.ss.android.ugc.aweme:id/af5").click()
    # 8.1
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/adu").click()
    # 点击用户进入用户搜索结果
    driver.find_elements_by_id("android:id/text1")[2].click()



    # 获取作者视频，点击第一个
    # el_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/bgx")
    # el_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/bkl")
    # 8.1
    el_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/biv")
    # for el in el_list:
    #     print(el.text)
    el_list[0].click()

    # 获取作品数量
    zuopin = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/title")
    if '作品' in zuopin[0].text:
        zuopin[2].click()
    else:
        zuopin[3].click()

    # video_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/a9h")
    # video_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/aac")
    # 8.1
    video_list = driver.find_elements_by_id("com.ss.android.ugc.aweme:id/a9x")

    num_str = zuopin.text.split()[-1]
    video_list[0].click()

    # 向上滑动屏幕
    if num_str.isdigit():
        num = int(num_str)
    else:
        # 如果获取不到作品数量，则设置为200
        num = 200
    print("%s有%d个喜欢" % (name,num))
    for i in range(num):

        # print(sc_size)
        x = sc_size.get('width')
        y = sc_size.get('height')
        driver.swipe(x*0.5,y*0.8,x*0.5,y*0.2)
        # print(driver.page_source)
        time.sleep(1)


    driver.quit()
    return name

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

