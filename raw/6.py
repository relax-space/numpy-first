'''
说明:
注:
    transpose:
    swapaxes:
    reshape: 可以替代上面的两个
概念: 
1. 维度:a=[[10,20],[30,40]] 这是一个二维数组,索引分别是0和1, 所以要取出40的值用 a[1,1],第一个1取出[30,40],第二个1取出40
2. 交换:通过交换索引来改变数据, 实际上交换索引不好理解,但是如果说是重新定义reshape的话就好理解了
'''
import numpy as np


def test_1():
    # 维度
    a1 = np.array([[10, 20], [30, 40]])
    assert 40 == a1[1, 1], 'np 维度 error'


def test_2():
    # 交换
    '''
    原先:
        索引 0  对应 shape是 2
        索引 1  对应 shape是3
    交换索引:
        注:交换索引即意味着交换shape
        shape:由原先的(2,3)变成(3,2)

    transpose swapaxes reshape 
        相同点: 都是变成shape(3,2)
        不同点:
            transpose: 竖着读,横着写
            swapaxes: 同上
            reshape: 当order='F'时, 竖着读,竖着写

    如果是三维,请参看: https://blog.csdn.net/ldm_666/article/details/107183244
    '''
    a1:np.ndarray = np.array([[10, 20, 30],
                   [40, 50, 60]])
    b1 = np.transpose(a1, [1, 0])
    c1 = np.swapaxes(a1, 0, 1)
    d1 = np.reshape(a1, (3, 2), order='F')

    assert [[10, 40], [20, 50], [30, 60]] == b1.tolist() and b1.tolist() == c1.tolist(), 'np reshape error'
    assert [[10, 50],
            [40, 30],
            [20, 60]] == d1.tolist(), 'np reshape 2 error'
