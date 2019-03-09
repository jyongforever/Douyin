# -*- coding:utf-8 -*-
import shutil
import os
import shutil

alist = []
def diguimulu(dir):
    if not os.path.isfile(dir):
        dirs = os.listdir(dir)
        for dir2 in dirs:
            diguimulu(dir + os.sep + dir2)

    else:
        new_dir = dir.replace('douyin','http:/')
        alist.append(new_dir[:new_dir.rfind('/')+1])
    return alist




