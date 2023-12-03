import pandas as pd
data = [1, 2, 3, 4, None]
index=['a','b','c','d','e']

s = pd.Series(data,index)

print(s.head(3)) #前3行  print(s.head())默认返回前 5 行
"""
a    1.0
b    2.0
c    3.0
dtype: float64
"""
print(s.tail (2)) #尾2行  #默认返回后 5 行
"""
d    4.0
e    NaN
dtype: float64
"""
print(pd.isnull(s)) #那个是空的？
"""
a    False
b    False
c    False
d    False
e     True
dtype: bool
"""
print(pd.notnull(s))  #拿个不空？
"""
a     True
b     True
c     True
d     True
e    False
dtype: bool
"""
