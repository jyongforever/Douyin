# -*- coding:utf-8 -*-
from hashlib import md5
m = md5()
from s_url import diguimulu
import requests

video_list = diguimulu('douyin')
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

for url in video_list:
    m.update(url.encode())
    print(url)
    with open('Video/%s.mp4' % m.hexdigest(),'wb') as f:
        res = requests.get(url)
        f.write(res.content)



