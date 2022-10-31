# -*- coding:utf-8 -*-
from src.primitive.vector import vector


class edge:
    # 构造函数
    def __init__(self, v1: vector, v2: vector):
        self.point_origin = v1
        self.point_end = v2

    def print_test(self):
        pass
        print(self.point_origin)
        print(self.point_end)

