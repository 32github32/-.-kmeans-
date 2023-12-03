

# 函数形式：dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# 参数：

# axis：轴。0或'index'，表示按行删除；
#          1或'columns'，表示按列删除。

# how：筛选方式。‘any’，表示该行/列只要有一个以上的空值，就删除该行/列；
#               ‘all’，表示该行/列全部都为空值，就删除该行/列。

# thresh：非空元素最低数量。int型，默认为None。
#         如果该行/列中，非空元素数量小于这个值，就删除该行/列。

# subset：子集。列表，元素为行或者列的索引。
#         如果axis=0或者‘index’，subset中元素为列的索引；
#         如果axis=1或者‘column’，subset中元素为行的索引。
#         由subset限制的子区域，是判断是否删除该行/列的条件判断区域。

# inplace：是否原地替换。布尔值，默认为False。
#          如果为True，则在原DataFrame上进行操作，返回值为None。

#创建DataFrame数据：
import numpy as np
import pandas as pd
 
a = np.ones((6,4))     # 创建一个形状为（6，4）的全1矩阵 6行4列 。内有多个list的list
for i in range(len(a)):  # len(a) = 11个list
    a[i,:i] = np.nan     # i行 0到i-1列是空值
 
d = pd.DataFrame(data=a)
print(d)
#      0    1    2    3
# 0  1.0  1.0  1.0  1.0
# 1  NaN  1.0  1.0  1.0
# 2  NaN  NaN  1.0  1.0
# 3  NaN  NaN  NaN  1.0
# 4  NaN  NaN  NaN  NaN
# 5  NaN  NaN  NaN  NaN

print(d.dropna(axis=0, how='any'))  #0就是行 # 按行删除：存在空值，即删除该行
#      0    1    2    3  错杀一千，不留一个
# 0  1.0  1.0  1.0  1.0

print(d.dropna(axis=0, how='all')) #  按行删除：所有数据都为空值，即删除该行
#      0    1    2    3
# 0  1.0  1.0  1.0  1.0
# 1  NaN  1.0  1.0  1.0
# 2  NaN  NaN  1.0  1.0
# 3  NaN  NaN  NaN  1.0

# 按列删除：该列非空元素小于3个的，即删除该列
print(d.dropna(axis='columns', thresh=3))
#      2    3
# 0  1.0  1.0
# 1  1.0  1.0
# 2  1.0  1.0
# 3  NaN  1.0
# 4  NaN  NaN
# 5  NaN  NaN

# 设置子集：删除第0、3列都为空的行
print(d.dropna(axis='index', how='all', subset=[0,3]))
#      0    1    2    3
# 0  1.0  1.0  1.0  1.0
# 1  NaN  1.0  1.0  1.0
# 2  NaN  NaN  1.0  1.0
# 3  NaN  NaN  NaN  1.0
#————————————————————————————————
# 4  NaN  NaN  NaN  NaN  0 和3列都是空值
# 5  NaN  NaN  NaN  NaN

# 设置子集：删除第1、3行存在空值的列
print(d.dropna(axis=1, how='any', subset=[1,3]))
#      3
# 0  1.0
# 1  1.0（不是空值）
# 2  1.0
# 3  1.0（不是空值）
# 4  NaN
# 5  NaN

# 原地修改
print(d.dropna(axis=0, how='any', inplace=True))
print("==============================")
print(d)

# None
# ==============================
#      0    1    2    3
# 0  1.0  1.0  1.0  1.0

# inplace：是否原地替换。布尔值，默认为False。
#          如果为True，则在原DataFrame上进行操作，返回值为None。【删完了】





"""

"""

  
