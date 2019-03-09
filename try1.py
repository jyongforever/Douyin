# -*- coding:utf-8 -*-
import time
import unittest



def add_num(a, b):
    return a + b


class TestCase01(unittest.TestCase):
    def test_add_num(self):
        result = add_num(1, 2)
        print("结果: ", result)

    def test_add_num02(self):

        result = add_num(1, 3)
        print("结果: ", result)


if __name__ == '__main__':
    unittest.main()
    t = time.strftime("%Y%m%d")
    print(t)

