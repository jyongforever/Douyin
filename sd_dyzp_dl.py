# -*- coding:utf-8 -*-
# 依赖test_douyin_zp.py,write_test_zp.py,rm_dumplicate.py
# 和s_url四个文件
import os
import shutil

from test_douyin_zp import video_url_download
from write_test_zp import video_write
from rm_dumplicate import rm_dump
shutil.rmtree("douyin")
os.mkdir("douyin")
author_name = input("请输入你要下载的作者名字")
video_write(author_name)
rm_dump('作品',author_name)
