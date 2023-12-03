# concat（）：左右连接、上下连接，取并集.
# merge（）：左右拼接、上下拼接，取交集，即同关键字的合并在一起。
# join（）：列方向拼接，即左右连接。
# append（）：行方向拼接，即上下连接。

"""
import os
import pandas as pd
location = r'. /myfiles'
data = pd.DataFrame ()
allfile = []
for root_dir, sub_dir,files in os.walk(location):
    for filename in files:
        if filename.endswith('xlsx'): #后缀
            temp = pd.read_excel(os.path.join(root_dir, filename))
            allfile. append (temp)
data = pd.concat(allfile)
data.to_excel(location+'/汇总表.xlsx') #location 可以是一个文件夹路径或者文件的前缀路径
"""
import pandas as pd

# 创建第一个表格
data1 = {'A': [1, 2, 3],
         'B': ['a', 'b', 'c']}
df1 = pd.DataFrame(data1)

# 创建第二个表格
data2 = {'A': [4, 5, 6],
         'B': ['d', 'e', 'f']}
df2 = pd.DataFrame(data2)

# 使用 concat() 函数将两个表格拼接
df_combined = pd.concat([df1, df2])

print(df_combined)

#    A  B
# 0  1  a
# 1  2  b
# 2  3  c
# 0  4  d
# 1  5  e
# 2  6  f









