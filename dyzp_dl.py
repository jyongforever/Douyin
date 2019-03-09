# -*- coding:utf-8 -*-
# 依赖test_douyin_zp.py,write_test_zp.py,rm_dumplicate.py
# 和s_url四个文件
from test_douyin_zp import video_url_download
from write_test_zp import video_write
from rm_dumplicate import rm_dump
author_name = video_url_download()
video_write(author_name)
rm_dump('作品',author_name)
