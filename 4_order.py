'''
说明: 读写顺序
1. reshape和T: 横读横写
2. reshape: order='F', 竖读竖写
3. transpose, swapaxes: 竖读横写
4. ravel+reshape: 各种组合,包括横读竖写
'''
import numpy as np


def test_1():
    # 技巧: 先算出shape,然后,往里面填充值
    a1 = np.array([[0,1,2], \
                   [3,4,5]])
    # 横读横写: 新的shape是三行两列(3,2)
    [[0,1], \
     [2,3], \
     [4,5]] == a1.reshape(3,2).tolist() == a1.T.tolist(), 'np error 3'

    # 竖读竖写: 新的shape是三行两列(3,2)
    [[0,4], \
     [3,2], \
     [1,5]] == a1.reshape(3,2,order='F').tolist(), 'np error 4'
    pass


def test_2():
    # 竖读横写: transpose, swapaxes
    a1 = np.array([[0,1,2], \
                   [3,4,5]])
    '''
    0轴: 第一个中括号是0轴
    1轴: 第二个中括号是1轴
    先计算shape为(3,2),np.transpose(a1, [1, 0]).shape
    然后,再竖读横写
    '''
    assert [[0, 3], \
            [1, 4], \
            [2, 5]] == np.transpose(a1).tolist() == \
    np.transpose(a1, [1, 0]).tolist() == np.swapaxes(a1,1,0).tolist(), 'np error 1'
    pass


def test_3():
    # 横读竖写
    a1 = np.array([[10,11,12,13], \
                   [14,15,16,17], \
                   [51,19,20,21], \
                   [22,23,24,25]])
    [[10,12,14,16,51,20,22,24], \
     [11,13,15,17,19,21,23,25],] == np.ravel(a1).reshape(2,8,order='F').tolist(),'np error 1'
    pass


def test_4():
    # 竖读横写: 3维,transpose
    '''
    0轴: 第一个中括号是0轴
    1轴: 第二个中括号是1轴
    2轴: 第三个中括号是2轴
    '''
    a1 = np.array([[[1, 2, 3], \
                    [4, 5, 6]], \
                   [[7, 8, 9], \
                    [10, 11, 12]]])

    assert (2, 2, 3) == a1.shape, 'np error 1'

    # 0轴不变, 交换1,2轴,第一个中括号不动
    assert (2, 3, 2) == np.transpose(a1, (0, 2, 1)).shape, 'np error 2'
    assert [[[1, 4], \
             [2, 5], \
             [3, 6]], \
            [[7, 10], \
             [8, 11], \
             [9, 12]]] == np.transpose(a1, (0, 2, 1)).tolist(), 'np error 3'

    # 2轴不变, 交换0,1轴,
    '''
    可以把[1,2,3]看成一个整体,对下面的竖读横写
    看到这里是不是豁然开朗啦
    a1 = np.array([[a123, a456], \
                   [a789, a101112]])
    '''
    [[[1, 2, 3], [7, 8, 9]], \
     [[4, 5, 6], [10, 11, 12]]] == np.transpose(a1, (1, 0, 2)).tolist(), 'np error 4'

    # (1,2,0) 3个轴都换了位置, 可以分两次来转换
    '''
    第一次: 1和0交换
    [[[1, 2, 3], [7, 8, 9]], \
     [[4, 5, 6], [10, 11, 12]]] == np.transpose(a1, (1, 0, 2)).tolist()
    第二次: 0和2交换,相当上面的0轴不变,后面两组数据做交换
    '''
    [[[1, 7], [2, 8], [3, 9]],
     [[4, 10], [5, 11],
      [6, 12]]] == np.transpose(a1, (1, 2, 0)).tolist(), 'np error 5'
    pass
