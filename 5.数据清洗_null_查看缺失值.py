"""
假设有如下的DataFrame对象df：

   A    B    C
0  1  NaN  3.0
1  4  5.0  NaN
2  7  8.0  9.0
"""
import pandas as pd

# 创建数据
data = {'A': [1, 4, 7], 
        'B': [None, 5, 8], 
        'C': [3, None, 9]}
df = pd.DataFrame(data)

# 检查缺失值
print(pd.isnull(df))
"""
运行上述代码，输出结果如下：

       A      B      C
0  False   True  False
1  False  False   True
2  False  False  False
"""

# 填充缺失值
df.fillna(0, inplace=True)
print(df)

"""
运行上述代码，输出结果如下：

   A    B    C
0  1  0.0  3.0
1  4  5.0  0.0
2  7  8.0  9.0
"""







