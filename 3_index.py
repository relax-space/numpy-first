'''
说明:索引
'''

import numpy as np


def test_1():
    # 一维
    a1 = np.array([0, 1, 2, 3, 4])
    assert 1 == a1[1], 'np error 1'
    pass


def test_2():
    '''
    二维: 左边第一个总括号是0维,第二个是1维
    说明: 下面例子是一个0维数组里面包含2个1维
    '''
    a1 = np.array([[0,1], \
                   [2,3]])
    assert [0, 1] == a1[0].tolist(), 'np error 1'

    assert 1 == a1[0, 1] == a1[0][1], 'np error 2'
    pass


def test_3():
    # 三维: 根据二维的思路理解即可
    a1 = np.array([[
                    [1, 2], \
                    [3, 4]], \
                   [[4, 5], \
                    [6, 7]]])

    assert [[1, 2], [3, 4]] == a1[0].tolist(), 'np error 1'

    assert [3, 4] == a1[0, 1].tolist(), 'np error 2'

    assert 4 == a1[0, 1, 1].tolist(), 'np error 3'

    pass
