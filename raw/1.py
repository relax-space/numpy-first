import numpy as np


def test_1():
    a1 = np.array([1, 2])
    assert [1, 2] == a1.tolist(), 'np init erro'


def test_2():
    # 数据类型
    t1 = np.dtype('i4')
    a1 = np.array([10, 12], dtype=t1)
    assert [10, 12] == a1.tolist(), 'np dtype error'


def test_3():
    # 数据类型: 结构化数据
    t1 = np.dtype([('name', 'a20'), ('age', 'i2')])
    a1 = np.array([('xiao', 19), ('xia', 18)], dtype=t1)
    assert 'xiao' == a1['name'][0].decode(
        'utf-8') and 18 == a1['age'][1], 'np dtype 2 error'


def test_4():
    # reshape: https://blog.csdn.net/u012435142/article/details/84404708
    a1 = np.arange(6).reshape(2, 3)
    assert [[0, 1, 2], [3, 4, 5]] == a1.tolist(), 'np reshape error'
    b1 = a1.reshape(3, 2)
    assert [[0, 1], [2, 3], [4, 5]] == b1.tolist(), 'np reshape 2 error'


def test_5():
    # reshape 2, 竖着读,竖着写, 比如写入第一列 0 4 ,然后写入第2列 8 12
    a1 = np.arange(16).reshape(4, 4)
    assert [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11],
            [12, 13, 14, 15]] == a1.tolist(), 'np reshape f error'
    b1 = np.reshape(a1, newshape=(2, 8), order='F')
    assert [[0, 8, 1, 9, 2, 10, 3, 11],
            [4, 12, 5, 13, 6, 14, 7,
             15]] == b1.tolist(), 'np reshape f 2 error'


def test_6():
    # ravel, 看看这种效果: https://www.xknote.com/blog/388832.html
    a1 = np.arange(16).reshape(4, 4)
    assert [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11],
            [12, 13, 14, 15]] == a1.tolist(), 'np ravel f 1 error'
    b1 = np.ravel(a1, order='F').reshape(2, 8)
    assert [[0, 4, 8, 12, 1, 5, 9, 13],
            [2, 6, 10, 14, 3, 7, 11, 15]] == b1.tolist(), 'np ravel f 2 error'

    c1 = np.ravel(a1).reshape(2, 8, order='F')
    assert [[0, 2, 4, 6, 8, 10, 12, 14],
            [1, 3, 5, 7, 9, 11, 13, 15]] == c1.tolist(), 'np ravel f 3 error'


def test_7():
    a1 = np.empty((2, 1), dtype='i4')
    assert a1[0][0] is not None and a1[1][0] is not None, 'np empty error'

    a1 = np.zeros((2, 1))
    assert [[0.], [0.]] == a1.tolist(), 'np zero error'

    a1 = np.ones((2, 1))
    assert [[1.], [1.]] == a1.tolist(), 'np ones error'
