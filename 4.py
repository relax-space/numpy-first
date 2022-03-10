import numpy as np


def test_1():
    a1 = np.arange(6).reshape(2, 3)
    assert [[0, 1, 2], [3, 4, 5]] == a1.tolist(), 'np nditer error'
    b1 = [i for i in np.nditer(a1)]
    assert [0, 1, 2, 3, 4, 5] == b1, 'np nditer error'
    c1 = [i for i in np.nditer(a1, order='F')]
    assert [0, 3, 1, 4, 2, 5] == c1, 'np nditer error'


def test_2():
    # 深度复制:copy
    # 浅复制:reshape : https://blog.csdn.net/S_o_l_o_n/article/details/108819034
    a1 = np.arange(6).reshape(2, 3)
    b1 = np.reshape(a1, (3, 2))
    c1 = a1.T
    d1 = np.copy(a1)
    a1[0][0] = 100
    assert [[100, 1], [2, 3], [4, 5]] == b1.tolist(), 'np copy error'
    assert [[100, 3], [1, 4], [2, 5]] == c1.tolist(), 'np copy 2 error'
    assert [[0, 1, 2], [3, 4, 5]] == d1.tolist(), 'np copy 3 error'
    
def test_3():
    # 读写数组
    a1 = np.arange(8).reshape(2,2,2)
    assert [[[0,1],[2,3]],[[4,5],[6,7]]]== a1.tolist(),'np rw error'
    for i in np.nditer(a1,op_flags=['readwrite']):
        # 这个地方其实不太明白,但是如果没有[...]原数组的值将不会翻倍
        i[...]=i*2
    assert [[[0,2],[4,6]],[[8,10],[12,14]]]== a1.tolist(),'np rw 2 error'
    

def test_4():
    # 同时迭代
    a1 = np.arange(4).reshape(2,2)
    b1 = np.array([10,20],dtype=int)
    c1 = [f'{x}:{y}' for x,y in np.nditer([a1,b1])]
    assert ['0:10','1:20','2:10','3:20']==c1,'np nditer multi error'
    
