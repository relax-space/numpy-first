'''
说明: 浅复制和深复制
    因为概念太多了, 视图, 副本,浅复制, 深复制
统一约定:
    浅复制: 能会修改原始数据的统称浅复制,即使没有复制操作
    深复制: 不会修改原始数据的统称深复制
1. reshape, T 和 copy, resize
2. nditer, flat,ravel(),flatten()
3. array 和 asarray
'''
import numpy as np


def test_1():
    '''
    深度复制: copy, resize
    浅复制: reshape, T
    '''
    a1 = np.array([[0, 1, 2], [3, 4, 5]])
    b1 = np.reshape(a1, (3, 2))
    c1 = a1.T
    d1 = np.copy(a1)
    e1 = np.resize(a1, (2, 3))
    a1[0, 0] = 100
    assert [[100, 1], [2, 3], [4, 5]] == b1.tolist(), 'np copy error'
    assert [[100, 3], [1, 4], [2, 5]] == c1.tolist(), 'np copy 2 error'
    assert [[0, 1, 2], [3, 4, 5]
            ] == d1.tolist() == e1.tolist(), 'np copy 3 error'
    pass


def test_2():
    '''
    深度复制: flatten()
    浅复制: flat, nditer(),ravel()
    '''
    a1 = np.arange(4).reshape(2, 2)
    b1 = a1.flat
    b2 = a1.ravel()
    b3 = np.nditer(a1)
    b4 = a1.flatten()
    a1[0][1] = 100
    assert [0, 100, 2, 3] == [i for i in b1] == b2.tolist() \
        == [i.tolist() for i in b3], 'np error 1'

    assert [0, 1, 2, 3] == b4.tolist(), 'np error 2'
    pass


def test_3():
    '''
    array() 和 asarray()的区别: 当参数是ndarray,并且没有指定dtype的时,后者不会复制新的,其他时候都会复制
    '''
    a1 = np.ones(3)
    assert np.ndarray == type(a1), 'np error 1'
    b1 = np.asarray(a1)
    c1 = np.array(a1)
    d1 = np.asarray(a1, dtype='i4')
    a1[1] = 2
    assert [1., 2., 1.] == a1.tolist() == b1.tolist(), 'np error 2'
    assert [1., 1., 1.] == c1.tolist() == d1.tolist(), 'np error 3'
