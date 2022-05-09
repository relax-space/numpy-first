import numpy as np


def test_1():
    # slice方法,切片,还有[...,1]切片,主要说一下 省略号的用法
    a1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    # 截取第2列,...等价于行索引ndarray [0,1,2]
    assert [1, 4, 7] == a1[..., 1].tolist() and [1, 4, 7] == a1[[0,1,2], 1].tolist(), 'np ... 1 error'
    # 截取第1行,...等价于列索引ndarray [0,1,2]
    assert [0, 1, 2] == a1[0, ...].tolist() and [0, 1, 2] == a1[0, [0,1,2]].tolist(), 'np ... 2 error'
    # 截取第2列和第3列
    assert [[1, 2], [4, 5], [7, 8]] == a1[..., 1:].tolist(), 'np ... 3 error'


def test_2():
    # 数组作为索引
    a1 = np.array([[1, 2], [3, 4]])
    b1 = a1[[0, 1], [1, 0]]
    assert [2, 3] == b1.tolist(), 'np slice 1 error'


def test_3():
    # 数组作为索引2: 获取矩阵的四个角
    a1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    rows = np.array([[0, 0], [3, 3]])
    cols = np.array([[0, 2], [0, 2]])
    b1 = a1[rows, cols]
    assert [[0, 2], [9, 11]] == b1.tolist(), 'np slice 2 error'


def test_4():
    # tile方法,如果能用广播尽量用广播
    a1 = np.array([1, 2])
    b1 = np.tile(a1, (2, 1))
    assert [[1, 2], [1, 2]] == b1.tolist(), 'np tile error'


def test_5():
    # 广播
    a1 = np.array([[1, 1], [1, 2], [1, 1]])
    b1 = np.array([2, 3])
    assert [[3, 4], [3, 5], [3, 4]] == (a1 + b1).tolist(), 'np broadcast error'
