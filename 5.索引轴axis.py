import pandas as pd
data = [1, 2, 3, 4, 5]
index=['a','b','c','d','e']
s = pd. Series (data,index) #先输数据，在输索引
print(s)
"""
a    1
b    2
c    3
d    4
e    5
"""
print(s.axes) #对象 s 的索引轴（axes）  行轴（axis 0）或列轴（axis 1）
"""
[Index(['a', 'b', 'c', 'd', 'e'], dtype='object')]
dtype='object' 表示数据类型为对象类型，通常用于存储字符串、Python 对象或混合类型的数据
"""
print(s.index)
#Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(s.values)
#[1 2 3 4 5]

#——————————————————————————————————————————
a = pd.Series([1, "apple", 3.5, 4], index = ['a','b', 'c', 'd'])
print(a)
"""
nmupy = 数值型
pandas = 数值型 + 非数值型
a        1
b    apple
c      3.5
d        4
"""

