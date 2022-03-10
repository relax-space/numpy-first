

import numpy as np


def test_1():
    # 广播
    a1 = np.array([[1], [2], [3]])
    b1 = np.array([5, 6, 7])
    bd = np.broadcast(a1, b1)
    '''
    第一步: b1 先广播成[[5,6,7],[5,6,7],[5,6,7]]
    第二步: a1 广播成[[1,1,1],[2,2,2],[3,3,3]]
    '''
    bd_add = [i+j for i, j in bd]
    c1 = np.array(bd_add).reshape(bd.shape)

    d1 = a1+b1

    assert [[6, 7, 8], [7, 8, 9], [8, 9, 10]] == d1.tolist(
    ) and c1.tolist() == d1.tolist(), 'np broadcast error'


def test_2():
    a1 = np.arange(4).reshape(1, 4)
    assert [[0, 1, 2, 3]] == a1.tolist(), 'np broadcast_to error'
    b1 = np.broadcast_to(a1, (4, 4))
    assert [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [
        0, 1, 2, 3]] == b1.tolist(), 'np broadcase_to error'


def test_3():

    a1 = np.arange(4).reshape(2, 2)
    assert [[0, 1], [2, 3]] == a1.tolist()
    # 第一个括号为0轴
    b1 = np.expand_dims(a1, axis=0)
    assert [[[0, 1], [2, 3]]] == b1.tolist(), 'np expand_dims error'
    # 第二个为1轴
    c1 = np.expand_dims(a1, axis=1)
    assert [[[0, 1]], [[2, 3]]] == c1.tolist(), 'np expand_dims 2 error'
    # 第三个括号为2轴
    d1 = np.expand_dims(b1, axis=2)
    assert [[[[0, 1]], [[2, 3]]]] == d1.tolist(), 'np expand_dims 3 error'


def test_4():
    # 挤压,只能挤压尺寸为1的轴, 比如下面的例子就不能传参数为axis=1,因为1轴 [[0, 1]], [[2, 3]]的尺寸为2(2维数组)
    a1 = np.array([[[[0, 1]], [[2, 3]]]])
    b1 = np.squeeze(a1, axis=0)
    assert [[[0, 1]], [[2, 3]]] == b1.tolist(), 'np squeeze error'
    c1 = np.squeeze(a1, axis=2)
    assert [[[0, 1], [2, 3]]] == c1.tolist(), 'np squeeze 2 error'
    

def test_5():
    a1 = np.array([[1],[2],[3]])
    b1 = np.array([1,2])
    assert [[2,3],[3,4],[4,5]] == (a1+b1).tolist(),'np broadcase 5 error'
    print(a1+b1)
