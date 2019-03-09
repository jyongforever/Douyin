# -*- coding:utf-8 -*-
f = open('test2.txt','w+')
f.write("aaa")
f.seek(0)
print(f.read())

