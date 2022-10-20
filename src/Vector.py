# -*- coding:utf-8 -*-

class vector(object):
    def __init__(self, *eles):
        assert len([e for e in eles if isinstance(e, (int, float))]) == len(eles)
        self.data = list(eles)

    def __repr__(self):
        return str(self.data)

    def __add__(self, other):
        assert isinstance(other, vector)
        la = len(self)
        lb = len(other)
        if la < lb:
            arr_a = self
            arr_b = other
        else:
            arr_a = other
            arr_b = self
        min_len = min(la, lb)

        return vector(*[e if i >= min_len else e + arr_a[i] for i, e in enumerate(arr_b)])

    def __sub__(self, other):
        return self + vector(*[-e for e in other])

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, key, value):
        if 0 <= key < len(self.data):
            self.data[key] = value

    def __len__(self):
        return len(self.data)

    def __iadd__(self, other):
        tmp = self + other
        self.data = tmp.data
        return self

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return vector(*[self.data[i] * other for i in range(len(self.data))])
        elif isinstance(other, vector):
            la = len(self.data)
            lb = len(other.data)
            if la < lb:
                arr_a = self
                arr_b = other
            else:
                arr_a = other
                arr_b = self
            min_len = min(la, lb)

            return vector(*[e if i >= min_len else e * arr_a[i] for i, e in enumerate(arr_b)])
        return self

    @property
    def x(self):
        return self[0] if len(self.data) >= 1 else 0

    @x.setter
    def x(self, val):
        if len(self.data) >= 1:
            self.data[0] = val

    @property
    def y(self):
        return self[1] if len(self.data) >= 2 else 0

    @y.setter
    def y(self, val):
        if len(self.data) >= 2:
            self.data[1] = val

    @property
    def z(self):
        return self[2] if len(self.data) >= 3 else 0

    @z.setter
    def z(self, val):
        if len(self.data) >= 3:
            self.data[2] = val

    @classmethod
    def dot(cls, a, b):
        if (not isinstance(a, vector)) or (not isinstance(b, vector)):
            raise Exception("a or b not vector type...")

        ret = 0
        for i, e in enumerate(a.data):
            ret += a[i] * b[i]
        return ret

    @classmethod
    def cross_product(cls, a, b):
        return cls(a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def test(v):
    import math
    t = abs(v.x) - abs(v.y)
    return vector(math.ceil(t) * v.x, abs(math.floor(t)) * v.y)


