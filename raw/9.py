'''

add
split
strip
join

'''

import numpy as np


def test_1():
    # add
    a1 = np.char.add(['hello'], [' numpy'])
    assert ['hello numpy'] == a1.tolist(), 'np add error'
    # 广播
    a2 = np.char.add([['hello', 'i']], [' numpy'])
    assert [['hello numpy', 'i numpy']] == a2.tolist(), 'np add 2 error'


def test_2():
    # split
    a1 = np.char.split(['hello numpy'])
    assert [['hello', 'numpy']] == a1.tolist(), 'np split error'
    # 不支持正则 \s+
    a2 = np.char.split('hello  numpy', r'  ')
    assert ['hello', 'numpy'] == a2.tolist(), 'np split 2 error'


def test_3():
    # strip
    a1 = np.char.strip('  abc', ' ')
    assert 'abc' == a1.tolist(), 'np strip error'


def test_4():
    # join
    a1 = np.char.join(':', ['ab', 'cd'])
    assert ['a:b', 'c:d'] == a1.tolist(), 'np join error'
