from vector import vector

if __name__ == '__main__':
    pass
    a = vector(-1, 1, 0)
    b = vector(1, 1, 0)
    c = vector(0, 0, 0)
    print("a和b的距离：", vector.distance(a, b))
    print("a的长度:", a.magnitude())
    print("标亮相乘：", a.mul_scalar(2))
    print("点成：", vector.dot(a, b))
    print("×乘", vector.cross(a, b))
    print("向量取反：", a.negative())
    print("平方长度:", a.sqr_magnitude())
    print("是否为0:", a.is_zero())
    print("是否为0:", c.is_zero())
    print("标准化：", a.normalize())
    print("获取两向量夹角:", vector.angle(a,b))
