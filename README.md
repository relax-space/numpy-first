# numpy-first


## 常用

1. 初始化 np.array([1]), np.arange(4).reshape(2,2)
2. 交换 reshape:竖读竖写, transpose,swapaxes, T : 竖读横写
3. array和asarray区别: 当参数是ndarray,并且没有指定dtype的时,asarray不会复制新的,其他时候都会复制
4. 省略号切片: a1[...,1]截取第2列,a1[0,...]截取第一行,a1[...,1:]截取第2列以后的行
5. 扁平: nditer, flat,ravel(),flatten(),其中深度复制是 flatten,其他不是
6. 拷贝: copy深度复制, 大多方法跟原始数组都有引用关系例如:reshape
7. 维度: [[1,2],[3,4]] 左边第一个括号是0维,第二个是1维
8. 广播: 两个数组,低维会向高维转换,原始:[[1], [2], [3]] 和[1,2], 第一步:[[1], [2], [3]] 和 [[1,2],[1,2],[1,2]],第二步:[[1,1], [2,2], [3,3]] 和 [[1,2],[1,2],[1,2]], 如果相加结果[[2,3],[3,4],[4,5]] 
9. 拆分: np.split(a1,2,0)是垂直, np.split(a1,2,1)是水平
10. 连接: concatenate(a1,a1,axis=0)是垂直,axis=1是水平
11. resize和reshape的区别: 前者是新的副本
12. 基本操作: append,insert,delete
13. 字符串: add strip split join



