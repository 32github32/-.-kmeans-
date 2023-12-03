"""

"""
import pandas as pd

# 创建一个示例 DataFrame
data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age' : [28, 34, 29, 42],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 使用 iloc 选择单个元素
print(df.iloc[0, 1])  # 选择第一行、第二列的元素（即 'Tom'） #28

# 使用 iloc 选择多行多列
print(df.iloc[0:2, 1:3])  # 选择前两行、第二到第三列的数据
"""
   Age           City
0   28       New York
1   34  San Francisco
"""
# 使用 iloc 选择特定行或列
print(df.iloc[[0, 2], [1, 2]])  # 选择第一行和第三行，以及第二列和第三列的数据
"""
   Age         City
0   28     New York
2   29  Los Angeles
"""



  
