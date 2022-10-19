# -*- coding:utf-8 -*-

'''
类方法，后续研究
@classmethod
    def get_name_1(cls):
        return "p"
'''


class m_vector:
    # 构造函数
    def __init__(self, *value):
        self.list_value = list(value)

    # 加
    def __add__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] + other.list_value[i])
        return m_vector(*current_list_value)

    # 减
    def __sub__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] - other.list_value[i])
        return m_vector(*current_list_value)

    # 乘
    def __mul__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] * other.list_value[i])
        return m_vector(*current_list_value)

    # 除
    def __truediv__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] / other.list_value[i])
        return m_vector(*current_list_value)

    # 打印
    def __str__(self):
        return str(self.list_value)

    # []
    def __getitem__(self, item):
        return self.list_value[item]

    # []=
    def __setitem__(self, key, value):
        self.list_value[key] = value

    # 点成
    @classmethod
    def dot(cls, v1, v2):
        cur_value = 0
        cur_value += v1[0] * v2[0]
        cur_value += v1[1] * v2[1]
        cur_value += v1[2] * v2[2]
        return cur_value

    # 叉乘
    @classmethod
    def cross(cls, v1, v2):
        return m_vector(v1[1] * v2[2] - v1[2] * v2[1],
                        v1[2] * v2[0] - v1[0] * v2[2],
                        v1[0] * v2[1] - v1[1] * v2[0])
