"""

"""
import pandas as pd

data=[['张明',10,160],
      ['李铁',22,288],
      ['王飞飞',33,399]
      ]                   #  #包含多个列表的列表 列就是列

"""
区别字典和但列表  行变列
data4 ={
        'Name':['Tom','Jack','Steve','Ricky'], #还给了表头columns
        'Age': [28, 34,29, 42]}
data1 = [1, 2, 3,"a",6.1,"奇怪"]
"""

df = pd. DataFrame (data, 
                    columns=['name', 'Age', 'total' ]) #多list 要自创表头
names=df['name'] #取name列,结果是series
print(names)
"""
0     张明
1     李铁
2    王飞飞
Name: name, dtype: object
"""
score=list(df["total"])  #取total列,结果是list,没索引
print(score)
"""
[160, 288, 399]
"""


  
