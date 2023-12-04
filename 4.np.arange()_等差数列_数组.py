"""
np.arange()是NumPy库中的一个函数，用于创建一个等差数列的一维数组。其语法为：
np.arange([start,] stop[, step,], dtype=None)
其中参数的含义如下：

start：可选参数，表示数列起始值，默认为0；
stop：必需参数，表示数列结束值（不包含该值）；
step：可选参数，表示数列的公差，默认为1；
dtype：可选参数，表示生成数组的数据类型。
"""


import numpy as np

# 创建一个从0到4的一维数组
arr1 = np.arange(5)
print(arr1)  # [0 1 2 3 4]

# 创建一个从1到9的一维数组，步长为2
arr2 = np.arange(1, 10, 2)
print(arr2)  # [1 3 5 7 9]

# 创建一个从0到1的一维数组，步长为0.1
arr3 = np.arange(0, 1, 0.1)
print(arr3)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]




