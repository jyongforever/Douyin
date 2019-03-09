# -*- coding:utf-8 -*-
# 1、abcd*9 = dcba abcd不重复
import time
import numpy

start = time.time()
for a in range(1, 10):

    for b in range(10):
        if b == a:
            continue
        for c in range(10):
            if c == a or c == b:
                continue
            for d in range(1, 10):
                if d == a or d == b or d == c:
                    continue
                if (a * 1000 + b * 100 + c * 10 + d) * 9 == d * 1000 + c * 100 + b * 10 + a:
                    print(a, b, c, d)
end = time.time()
print(end - start)


# 2、1、	一个房间中有4个人A、B、C、D，他们当中一个人在玩游戏，
# 一个人在看手机，一个人在座瑜伽，另一个人在听音乐，其中：
# A 不在玩游戏，也不在听音乐；
# B 不在做瑜伽，也不在玩游戏；
# 如果A不在做瑜伽，那么D不在玩游戏；
# C不在听音乐，也不在玩游戏；
# D不在听音乐，也不在做瑜伽
# 问：他们各自在做什么？
alist = ['游戏','手机','瑜伽','音乐']
for a in alist:
    if a == '游戏' or a == '音乐':
        continue
    for b in alist:
        if b == '瑜伽' or b == '游戏' or b == a:
            continue
        for c in alist:
            if c == '音乐' or c == '游戏' or c == b or c == a:
                continue
            for d in alist:
                if d == '音乐' or d == '瑜伽' or d == a or d == b or d == c:
                    continue
                if a != '瑜伽':
                    if d == '游戏':
                        continue
                print(a,b,c,d)



# 1、	请使用Python写一个交换机批量创建vlan的脚本，
# 如：vlan从100创建到1000，只创建奇数，偶数不创建，
# vlan name为hxat*(*为100到1000的ID)，
# 每条创建成功请打印提示信息，如：创建vlan hxat100成功。交换机命令行示例为：
# config terminal
# create vlan vlan100

for i in range(100,1000):
    if i % 2 !=0:
        print('create vlan vlan%s' % i)









