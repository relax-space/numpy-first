'''
说明: 扁平
'''

import numpy as np


def test_1():
    # 几种扁平方法: flat,ravel,nditer,flatten
    a1 = np.arange(4).reshape(2, 2)
    b1 = a1.flat
    b2 = a1.ravel()
    b3 = np.nditer(a1)
    b4 = a1.flatten()
    assert [0, 1, 2, 3] == [i for i in b1] == b2.tolist() \
        == [i.tolist() for i in b3] == b4.tolist(), 'np error 1'
    pass


def test_2():
    # nditer 2维
    a1 = np.array([[0, 1], \
                   [2, 3]])
    assert [0, 1, 2, 3] == [i.tolist() for i in np.nditer(a1)], 'np error 1'
    # 竖读
    assert [0, 2, 1,
            3] == [i.tolist() for i in np.nditer(a1, order='F')], 'np error 2'
    pass


def test_3():
    # nditer 3维
    a1 = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
    assert [0, 1, 2, 3, 4, 5, 6,
            7] == [i.tolist() for i in np.nditer(a1)], 'np error 1'

    # 坐标对应关系
    assert [[[0, 1], [2, 3]],
            [[4, 5], [6, 7]]] == [[[a1[0, 0, 0], a1[0, 0, 1]],
                                   [a1[0, 1, 0], a1[0, 1, 1]]],
                                  [[a1[1, 0, 0], a1[1, 0, 1]],
                                   [a1[1, 1, 0], a1[1, 1, 1]]]], 'np error 2'
    '''
    存储顺序如下:
    第1片内存区: 2轴坐标为0, 行: 0轴, 列: 1轴
    [0, 0, 0]=0 [0, 1, 0]=2
    [1, 0, 0]=4 [1, 1, 0]=6
    
    第2片内存区: 2轴坐标为1, 行: 0轴, 列: 1轴
    [0, 0, 1]=1 [0, 1, 1]=5
    [1, 0, 1]=3 [1, 1, 1]=7
    '''
    # 竖读
    assert [0, 4, 2, 6, 1, 5, 3,
            7] == [i.tolist() for i in np.nditer(a1, order='F')], 'np error 2'
    pass


def test_4():
    # 迭代多个
    a1 = np.array([[0, 1], [2, 3]])
    b1 = np.array([10, 20])

    assert ['0:10', '1:20', '2:10',
            '3:20'] == [f'{i}:{j}' for i, j in np.nditer([a1, b1])]


def test_5():
    # 读写数组
    a1 = np.arange(8).reshape(2, 2, 2)
    assert [[[0, 1], [2, 3]], [[4, 5], [6, 7]]] == a1.tolist(), 'np rw error'
    for i in np.nditer(a1, op_flags=['readwrite']):
        # 等价于 不建议使用: i[...] = i * 2, 因为官方没有解释,人类无法理解
        i.setfield(i * 2, dtype=np.int32)
    assert [[[0, 2], [4, 6]], [[8, 10], [12,
                                         14]]] == a1.tolist(), 'np rw 2 error'


def test_6():
    # 内存数据: 行主序
    raw = [[1, 2], \
           [3, 4]]
    '''
    a1: order='C', 行主序, 横向存储, 
        存储顺序:1,2,3,4, 先存1,然后存2...
        1,2存储在连续的内存
    1 2
    → →
    3 4
    → →
    '''
    a1 = np.array(raw, order='C')
    # 按照存储的顺序取值
    assert [1, 2, 3, 4] == [i.tolist() for i in np.nditer(a1)], 'np error 1'
    # 横向读取:速度快, 因为读取的是连续内存
    assert [1, 2, 3,
            4] == [i.tolist() for i in np.nditer(a1, order='C')], 'np error 2'
    # 竖向读取
    assert [1, 3, 2,
            4] == [i.tolist() for i in np.nditer(a1, order='F')], 'np error 3'
    # 按存储顺序取值
    assert [[1, 2, 3, 4]
            ] == [i.tolist() for i in np.nditer(a1, flags=['external_loop'])
                  ], 'np error 4'
    # 横向取值
    assert [[1, 2, 3, 4]] == [
        i.tolist() for i in np.nditer(a1, flags=['external_loop'], order='C')
    ], 'np error 5'
    # 竖向取值
    assert [[1, 3], [2, 4]] == [
        i.tolist() for i in np.nditer(a1, flags=['external_loop'], order='F')
    ], 'np error 6'


def test_7():
    # 内存数据: 列主序
    raw = [[1, 2], \
           [3, 4]]
    a1 = np.array(raw, order='F')
    '''
    a1: order='F', 列主序, 竖向存储, 
        存储顺序:1,3,2,4, 先存1,然后存3...
        1,3存储在连续的内存
    1 ↓ 2 ↓
    3 ↓ 4 ↓
    '''
    # 按照存储的顺序取值
    assert [1, 3, 2, 4] == [i.tolist() for i in np.nditer(a1)], 'np error 1'
    # 横向取值
    assert [1, 2, 3,
            4] == [i.tolist() for i in np.nditer(a1, order='C')], 'np error 2'
    # 竖向取值: 速度快, 因为读取的是连续内存
    assert [1, 3, 2,
            4] == [i.tolist() for i in np.nditer(a1, order='F')], 'np error 3'

    assert [[1, 3, 2, 4]
            ] == [i.tolist() for i in np.nditer(a1, flags=['external_loop'])
                  ], 'np error 4'
    # 将不是连续内存块的数据, 一次性读出来
    assert [[1, 2], [3, 4]] == [
        i.tolist() for i in np.nditer(a1, flags=['external_loop'], order='C')
    ], 'np error 5'

    assert [[1, 3, 2, 4]] == [
        i.tolist() for i in np.nditer(a1, flags=['external_loop'], order='F')
    ], 'np error 6'
