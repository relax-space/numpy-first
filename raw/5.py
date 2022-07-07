import numpy as np


def test_1():
    # nditer 和 flat的区别, 基本上nditer可以包括flat的功能
    a1 = np.arange(4).reshape(2, 2)
    assert [[0, 1], [2, 3]]
    b1 = [i.tolist() for i in np.nditer(a1)]
    c1 = [i for i in a1.flat]
    assert [0, 1, 2, 3] == b1 == c1, 'np flat error'


def test_2():
    # flatten 深复制 和 ravel 浅视图
    a1 = np.arange(4).reshape(2, 2)
    b1 = a1.flat
    c1 = a1.flatten()
    d1 = a1.ravel()
    a1[0][1] = 100
    print(b1, c1,d1)
    assert [0, 100, 2, 3] == [i for i in b1], 'np flatten 2 error'
    assert [0, 1, 2, 3] == c1.tolist(), 'np flatten error'
    assert [0, 100, 2, 3] == d1.tolist(), 'np flatten 2 error'
