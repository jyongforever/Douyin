# -*- coding:utf-8 -*-
import requests
url = "http://v1-dy.ixigua.com/43e221fc6d99cab8df072a59bef062b8/5c2c77c9/video/m/22073f9f4b4ae994844853feb015231dae211613245d00003f05a95f6050/"
res = requests.get(url)

with open('t.mp4','wb') as f:
    f.write(res.content)



