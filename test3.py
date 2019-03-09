# -*- coding:utf-8 -*-
s = 'Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=491,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,Error=200,Error=201,Error=501,'

import re

res = re.findall('Error=\d+',s)
print(res)
print(len(res))

for i in range(256):
    print(chr(i),end='')


