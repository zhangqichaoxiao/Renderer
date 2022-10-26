from m_vector import m_vector

if __name__ == '__main__':
    pass
    a = m_vector(1, 0, 0)
    b = m_vector(-1, 1, 0)
    import math
    print(math.degrees(m_vector.angle(a, b)))
    # print(m_vector.dot(a, b))
    # print(m_vector.magnitude(a))
    # print(m_vector.magnitude(b))
