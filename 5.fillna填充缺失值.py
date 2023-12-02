import pandas as pd

# 创建一个包含 NaN 值的数据帧
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8]})

# 用每列的均值填充缺失值
df.fillna(df.mean(), inplace=True)

# 输出结果
print(df)

"""
     A    B
0  1.0  5.0
1  2.0  6.7
2  2.333333  7.0
3  4.0  8.0
"""



import pandas as pd

# 创建一个包含 NaN 值的数据帧
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8]})

# 用指定的值填充缺失值
df.fillna(0, inplace=True)

# 输出结果
print(df)

"""
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  8.0
"""


python
import pandas as pd

# 创建一个包含 NaN 值的数据帧
df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, 8]})

# 使用前一个非缺失值填充缺失值
df.fillna(method='ffill', inplace=True)

# 输出结果
print(df)


"""
     A    B
0  1.0  5.0
1  2.0  5.0
2  2.0  7.0
3  4.0  8.0
"""










