# -*- coding:utf-8 -*-
import math

# Fixed: 类名修改，不加m_前缀
class vector:
    # 构造函数
    def __init__(self, *value):
        self.list_value = list(value)

    # 打印
    def __str__(self):
        return str(self.list_value)

    # []
    def __getitem__(self, item):
        return self.list_value[item]

    # []=
    def __setitem__(self, key, value):
        self.list_value[key] = value

    # 向量加法
    def __add__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] + other.list_value[i])
        return vector(*current_list_value)

    # 向量减法
    def __sub__(self, other):
        current_list_value = []
        for i in range(3):
            current_list_value.append(self.list_value[i] - other.list_value[i])
        return vector(*current_list_value)

    # 两点距离
    @classmethod
    def distance(cls, v1, v2):
        cur_vector = v1 - v2
        # Fixed: 可以直接返回cur_vector.magnitude(), 不必引入中间变量
        return cur_vector.magnitude()

    # 标量相乘
    def mul_scalar(self, f1):
        return vector(self[0] * f1, self[1] * f1, self[2] * f1)

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
        return vector(v1[1] * v2[2] - v1[2] * v2[1],
                      v1[2] * v2[0] - v1[0] * v2[2],
                      v1[0] * v2[1] - v1[1] * v2[0])

    # 向量取反
    def negative(self):
        return vector(self.list_value[0] * -1, self.list_value[1] * -1, self.list_value[2] * -1)

    # 向量长度
    def magnitude(self):
        # Fixed: 考虑复用sqr_magnitude的结果
        return math.sqrt(self.sqr_magnitude())

    # 平方长度
    def sqr_magnitude(self):
        # Fixed: 平方考虑直接相乘
        return self.list_value[0] * self.list_value[0] + self.list_value[1] * self.list_value[1] + self.list_value[2] * \
               self.list_value[2]

    # 是否为0
    def is_zero(self):
        # Fixed: 浮点数和0的比较问题
        if self.list_value[0] <= 1e-5 and self.list_value[1] <= 1e-5 and self.list_value[2] <= 1e-5:
            return True
        return False

    # 标准化
    def normalize(self):
        return self.mul_scalar(1 / self.magnitude())

    # 获取两向量夹角：弧度即可
    @classmethod
    def angle(cls, v1, v2):
        numerator = cls.dot(v1, v2)
        denominator = v1.sqr_magnitude() * v2.sqr_magnitude()
        return math.acos(math.sqrt(numerator * numerator / denominator) * (1 if numerator > 0 else -1))
