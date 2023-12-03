"""

"""
import pandas as pd

# 创建一个示例 DataFrame
data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age' : [28, 34, 29, 42],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 使用 iloc 选择单个元素
print(df.iloc[0, 1])  # 选择第一行、第二列的元素（即 'Tom'） #28

print(df.iloc[:,0:2]) #切前两列
"""
    Name  Age
0    Tom   28
1   Jack   34
2  Steve   29
3  Ricky   42
"""
print(df.iloc[0:2,:])#切前两行
"""
   Name  Age           City
0   Tom   28       New York
1  Jack   34  San Francisco
"""











  
