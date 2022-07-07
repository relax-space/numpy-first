'''
说明: 创建, 增删改查
'''

import numpy as np


def test_1():
    a1 = np.array([1, 2])
    assert [1, 2] == a1.tolist() and np.ndarray == type(a1), 'np error 1'


def test_2():
    # 指定数据类型
    a1 = np.array([1, 2], dtype=np.int32)
    assert [1, 2] == a1.tolist() and np.int32 == type(a1[0]), 'np error 2'


def test_3():
    # 指定结构化数据
    t1 = np.dtype = [('name', np.unicode_, 20), ('age', np.int16)]
    a1 = np.array([('xiao', 19), ('xia', 18)], dtype=t1)
    print(a1)
    pass


def test_4():
    a1 = np.empty((2, 1))
    # ndim:维度, shape: 几行几列, size: 行 乘以 列
    assert 2 == a1.ndim and (2, 1) == a1.shape and 2 == a1.size, 'np error 1'
    a1 = np.zeros(2)
    assert [0, 0] == a1.tolist(), 'np error 2'
    a1 = np.zeros((2, 1))
    assert [[0.], [0.]] == a1.tolist(), 'np error 3'
    a1 = np.ones((2, 1))
    assert [[1.], [1.]] == a1.tolist(), 'np error 4'
    a1 = np.arange(2)
    assert [0, 1] == a1.tolist(), 'np error 5'
    # 0~5 前闭后开, 每隔两个索引取一次值
    a1 = np.arange(0, 5, 2)
    assert [0, 2, 4] == a1.tolist(), 'np error 6'

    a1 = np.arange(6).reshape(2, 3)
    assert [[0, 1, 2], [3, 4, 5]] == a1.tolist(), 'np error 7'
