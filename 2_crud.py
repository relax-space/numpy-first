'''
说明: 增删改查
'''
import numpy as np


def test_1():
    # 增加: append
    a1 = np.array([[1], [2], [3]])
    a2 = np.array([[4], [5]])
    assert [1, 2, 3, 4, 5] == np.append(a1, a2).tolist(), 'np error 1'
    assert [[1], [2], [3], [4],
            [5]] == np.append(a1, a2, axis=0).tolist(), 'np error 2'

    a3 = np.array([[4], [5], [6]])
    assert [[1, 4], [2, 5], [3, 6]] == np.append(a1, a3,
                                                 axis=1).tolist(), 'np error 3'


def test_2():
    # 删除: delete
    a1 = np.array([[1, 2], [3, 4], [5, 6]])
    b1 = np.delete(a1, 1)
    assert [1, 3, 4, 5, 6] == b1.tolist() and [[1, 2], [3, 4], [5, 6]
                                               ] == a1.tolist(), 'np error 1 '

    b1 = np.delete(a1, 1, axis=0)
    assert [[1, 2], [5, 6]] == b1.tolist(), 'np error 2 '

    b1 = np.delete(a1, 1, axis=1)
    assert [[1], [3], [5]] == b1.tolist(), 'np error 3 '
    pass


def test_3():
    # 修改
    a1 = np.array([[1, 2], [3, 4]])
    a1[0] = [100, 1]
    assert [[100, 1], [3, 4]] == a1.tolist(), 'np error 1'

    a1[0, 1] = 5
    assert [[100, 5], [3, 4]] == a1.tolist(), 'np error 2'


def test_4():
    # 查询
    a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert 1 == a1[0, 0], 'np error 1'
    assert [[1, 2, 3], [4, 5, 6]] == a1[0:2].tolist() == a1[
        0:2, :].tolist() == a1[0:2, ...].tolist(), 'np error 2'
    assert [[2, 3], [5, 6], [8, 9]
            ] == a1[:, 1:].tolist() == a1[..., 1:].tolist(), 'np error 3'


def test_5():
    '''
    广播: + 和 add操作的时候, 会广播, 低维向高维转换, 并对齐
    广播过程分析:
        1.原始: [[1], [2], [3]] 和 [1, 2]
        2.低转高并对齐: [[1], [2], [3]] 和 [[1, 2],[1, 2],[1, 2]]
        3.对齐: [[1,1], [2,2], [3,3]] 和 [[1, 2],[1, 2],[1, 2]]
    '''
    a1 = np.array([[1], [2], [3]])
    a2 = np.array([1, 2])
    assert [[2, 3], [3, 4], [4, 5]] == (a1 + a2).tolist() == np.add(
        a1, a2).tolist(), 'np error 1'


def test_6():
    '''
    结论: append 可以完全替代vstack, hstack, concatenate
    源码: vstack, hstack 和 append都调用了concatenate
    '''
    a1 = [[1, 2], [3, 4]]
    a2 = [[5, 6], [7, 8]]
    assert [[1, 2], [3, 4], [5, 6], [7, 8]] == np.append(
        a1, a2, axis=0).tolist() == np.concatenate(
            (a1, a2)).tolist() == np.vstack((a1, a2)).tolist(), 'np error 1'
    assert [[1, 2, 5, 6], [3, 4, 7, 8]] == np.append(
        a1, a2, axis=1).tolist() == np.concatenate(
            (a1, a2), axis=1).tolist() == np.hstack(
                (a1, a2)).tolist(), 'np error 2'


def test_7():
    '''
    查询: where
        numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
    '''
    a1 = np.array([[1, 2, 3], \
                   [4, 5, 6], \
                   [7, 8, 9]])
    # 先来个完整的例子, 再逐步解释, 最后一个0会广播
    res = np.where(a1 > 4, a1, 0)
    assert [[0, 0, 0], [0, 5, 6], [7, 8, 9]] == res.tolist(), 'np error 1'

    # 解释1: where返回的是索引
    b1 = np.where(a1 > 8)
    assert 9 == a1[b1] == a1[[2], [2]] == a1[2, 2] == a1[(
        2, 2)] == a1[np.array([2]), np.array([2])], 'np error 2'

    # 解释2: where返回的是索引,同时结果会平铺
    b1 = np.where(a1 > 5)
    # b1[0]代码行索引, b1[1]代码列索引
    assert [1, 2, 2, 2] == b1[0].tolist() and [
        2, 0, 1, 2
    ] == b1[1].tolist(), 'np error 3'
    assert [6, 7, 8, 9] == a1[b1].tolist(), 'np error 4'

    # 解释3: 条件成立从第二个参数取值, 条件不成立从第三个参数取值
    assert [[1, 8], [3,4]] == np.where([[True, False], [True, True]], \
                                [[1, 2], [3, 4]],
                              [[9, 8], [7, 6]]).tolist(), 'np error 1'
    pass
