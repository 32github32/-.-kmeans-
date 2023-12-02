
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 提取第一行数据
row1 = df.iloc[0]

#第一列
#ID = data.iloc[:, 0]  #提出表格第一列的内容

# 打印第一行数据
print(row1)

