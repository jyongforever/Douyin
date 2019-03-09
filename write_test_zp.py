# -*- coding:utf-8 -*-
import os
import time


def video_write(author_name):
    if not os.path.exists("Video/作品/%s" % author_name):
        os.makedirs("Video/作品/%s" % author_name)
    # 记录下载过的视频url
    # v = open('video.txt','a+')
    # v.seek(0)
    # v_list = v.read().split()
    # print(v_list)
    from hashlib import md5
    m = md5()
    from s_url import diguimulu
    import requests

    video_list = diguimulu('douyin')
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    n = 0
    for url in video_list:
        start = time.time()
        print("还剩%s个视频未下载" % (len(video_list) - n))
        m.update(url.encode())
        vname = m.hexdigest()
        # if vname not in v_list:
        host_url = url.split('/video')[0]
        headers.update({"Host":host_url})
        # v.write(vname + '\n')
        with open('Video/作品/%s/%s.mp4' % (author_name,vname),'wb') as f:
            res = requests.get(url)
            content_size = int(res.headers['content-length'])
            # print(content_size)
            print(vname, url)
            print('[文件大小]：%0.2f MB' % (content_size/1024/1024))
            if content_size == 169 or content_size == 0:
                os.remove('Video/作品/%s.mp4' % vname)
                print("无法播放视频已删除")
                continue
            f.write(res.content)
        n += 1

        # else:
        #     print('视频已下载')
        print("用时%.2f秒"% (time.time() - start))
    print("共%s个视频下载完毕" % n)

