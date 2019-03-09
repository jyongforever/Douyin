# -*- coding:utf-8 -*-
import os
from hashlib import md5

# 根据视频内容，删除重复视频
def rm_dump(type_,author_name):
    alist = []
    # 获取已下载视频名称列表
    vlist = os.listdir('Video/%s/%s/' % (type_,author_name))
    # print(vlist)

    # 遍历视频名称列表，将视频内容用md5加密，添加到一个新列表alist中
    for v in vlist:
        m = md5()
        f = open('Video/%s/%s/' % (type_,author_name) + v,'rb')
        data = f.read()
        m.update(data)
        alist.append(m.hexdigest())
    # print(len(vlist))
    # print(len(alist))
    # print(len(set_alist))
    new_alist = []
    new_vlist = []
    # 遍历md5加密的视频内容列表，将不重复的加入到新列表new_alist中

    for n,t in enumerate(alist):
        if t not in new_alist:
            new_alist.append(t)
            new_vlist.append(vlist[n])
        else:
            # # 重复的文件删除掉
            print("删除重复视频%s" % vlist[n])
            os.remove('Video/%s/%s/' % (type_,author_name) + vlist[n])



