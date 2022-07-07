import numpy as np


def test_1():
    # array() 和 asarray()的区别: 当参数是ndarray,并且没有指定dtype的时,后者不会复制新的,其他时候都会复制
    # https://www.cnblogs.com/Renyi-Fan/p/13773546.html
    a1 = np.ones(3)
    b1 = np.array(a1)
    c1 = np.asarray(a1)
    a1[1] = 2
    assert [1., 2., 1.] == a1.tolist(), 'np asarray 1 error'
    assert [1., 1., 1.] == b1.tolist(), 'np asarray 2 error'
    assert [1., 2., 1.] == c1.tolist(), 'np asarray 3 error'


def test_2():
    it = iter([1, 2])
    a1 = np.fromiter(it, dtype='i4')
    assert [1, 2] == a1.tolist(), 'np fromiter error'


def test_3():
    # 等差数列 linspace
    # 2到3分成距离相等的5个数字, 很显然应该是(3-2)/(5-1)= 0.25
    a1 = np.linspace(2, 3, num=5)
    assert [2., 2.25, 2.5, 2.75, 3] == a1.tolist(), 'linspace 1 error'

    # 2到3分成距离相等的5个数字,不包括最后一个数字, 很显然应该是(3-2)/5= 0.2
    a1 = np.linspace(2, 3, num=5, endpoint=False)
    assert [2., 2.2, 2.4, 2.6, 2.8] == a1.tolist(), 'linspace 2 error'
    # 会返回等差的值
    a1 = np.linspace(2, 3, num=5, retstep=True)
    assert [2., 2.25, 2.5, 2.75, 3] == a1[0].tolist(
    ) and 0.25 == a1[1], 'linspace 2 error'


def test_4():
    # 等比数列: 其实就是把等差数列的间距值当做幂,比如等差为 2.,2.25,2.5,2.75,3,那么就是10的2.次方,10的2.25次方...
    base = 10
    a1 = np.linspace(2, 3, num=5)
    # a1= [2.,2.25,2.5,2.75,3]
    exp = []
    for i in a1:
        exp.append(base**i)

    b1 = np.logspace(2, 3, num=5, base=base)
    # b1=[100.0, 177.82794100389228, 316.22776601683796, 562.341325190349, 1000.0]
    assert exp == b1.tolist(), 'np logspace error'

    a1 = 'abc'
    print(a1[1:])
