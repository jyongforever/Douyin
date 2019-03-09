# -*- coding:utf-8 -*-
# 依赖test_douyin_xh.py,write_test_xh.py,rm_dumplicate.py
# 和s_url四个文件
from test_douyin_xh import video_url_download
from write_test_xh import video_write
from rm_dumplicate import rm_dump
author_name = video_url_download()
video_write(author_name)
rm_dump('喜欢',author_name)
