

import numpy as np


def test_1():
    a1 = np.arange(16).reshape(4, 4)
    assert [[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]] == a1.tolist()
    b1 = np.split(a1, 2)
    b2 = np.vsplit(a1, 2)
    b11 = [i.tolist() for i in b1]
    b21 = [i.tolist() for i in b2]

    assert [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[8, 9, 10, 11], [12, 13, 14, 15]]
    ] == b11 and b11 == b21, 'np split error'

    c1 = np.split(a1, 2, 1)
    c2 = np.hsplit(a1, 2)
    c11 = [i.tolist() for i in c1]
    c21 = [i.tolist() for i in c2]
    assert [
        [[0, 1], [4, 5], [8, 9], [12, 13]],
        [[2, 3], [6, 7], [10, 11], [14, 15]]
    ] == c11 and c11 == c21, 'np split 2 error'


def test_2():
    a1 = np.array([[0, 1],
                   [2, 3]])
    a2 = np.array([[4, 5],
                   [6, 7]])

    b1 = np.concatenate((a1, a2))
    b2 = np.vstack((a1, a2))
    assert [[0, 1], [2, 3], [4, 5], [6, 7]] == b1.tolist(
    ) and b1.tolist() == b2.tolist(), 'np concatenate error'

    c1 = np.concatenate((a1, a2), axis=1)
    c2 = np.hstack((a1, a2))
    assert [[0, 1, 4, 5], [2, 3, 6, 7]] == c1.tolist(
    ) and c1.tolist() == c2.tolist(), 'np concatenate error'


def test_3():
    # resize
    a1 = np.array([[0, 1, 2], [3, 4, 5]])

    b1 = np.reshape(a1, (3, 2))
    c1 = np.resize(a1, (3, 2))

    a1[0][0] = 100

    assert [[100, 1], [2, 3], [4, 5]] == b1.tolist(), 'np resize error'
    assert [[0, 1], [2, 3], [4, 5]] == c1.tolist(), 'np resize 2 error'


def test_4():
    # resize 2, 新数组大于原数组时,会重复
    a1 = np.array([[0, 1], [2, 3]])

    b1 = np.resize(a1, (2, 3))

    assert [[0, 1, 2], [3, 0, 1]] == b1.tolist(), 'np resize 3 error'

    c1 = np.resize(a1, (5, 2))
    assert [[0, 1], [2, 3], [0, 1], [2, 3], [
        0, 1]] == c1.tolist(), 'np resize 4 error'


def test_5():
    a1 = np.array([[1, 2], [3, 4]])

    b1 = np.append(a1, [5, 6])

    c1 = np.append(a1, [[5, 6]])

    d1 = np.append(a1, [[[5]], [[6]]])

    e1 = np.append(a1, [[5], [6]], axis=1)

    assert b1.tolist() == c1.tolist() == d1.tolist() and [
        1, 2, 3, 4, 5, 6] == b1.tolist(), 'np append error'

    assert [[1, 2, 5], [3, 4, 6]] == e1.tolist(), 'np append 2 error'
