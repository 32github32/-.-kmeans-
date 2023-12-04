

import pandas as pd
data = [1, 2, 3, 4, 5]
index=['a','b','c','d','e']
s = pd. Series (data, index)
print(s)
# a    1
# b    2
# c    3
# d    4
# e    5  【所以，最好把索引也打上】
# dtype: int64  # dtype 数据类型

print(s.axes)      #[Index(['a', 'b', 'c', 'd', 'e'], dtype='object')]  
#对于一维的Series对象，它只有一个轴，即索引轴；
#而对于二维的DataFrame对象，它有两个轴，分别是行轴和列轴。


print(s.index)     #Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
#打印索引

print(s.values)    #[1 2 3 4 5]    
#打印值




data = [1, 2, 3,4,5]
df = pd. DataFrame (data)
print(df)
#    0  【和 Series 区别 在于 表头 没有索引】
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5  


data=[['张明',10],
      ['李铁',12],
      ['王飞飞',13]]
df = pd.DataFrame(data,columns=['name','Age'],index = ['a','b','c'])
print(df)
#   name  Age
# a   张明   10
# b   李铁   12
# c  王飞飞   13


df2 = pd.DataFrame(data,columns=('name','Age'))
print(df2.index)
#RangeIndex(start=0, stop=3, step=1)
#返回DataFrame df2的行索引信息，它可以帮助你了解DataFrame中行的标签或者编号，从而更好地理解和处理数据。
#区别 print(s.index)     #Index(['a', 'b', 'c', 'd', 'e'], dtype='object')





