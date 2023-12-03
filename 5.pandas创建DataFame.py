import pandas as pd

#列表创建DataFame
data1 = [1, 2, 3,"a",6.1,"奇怪"]
df1 = pd.DataFrame(data1)
print(df1)
"""
     0
0    1
1    2
2    3
3    a
4  6.1
5   奇怪
"""
                       #包含多个列表的列表
data2=[
       ['张明',10],
       ['李铁',12],
       ['王飞飞',13]
       ]
df2 = pd. DataFrame (data2,columns=['name', 'Age']) #给列命名
print(df2)
"""
  name  Age
0   张明   10
1   李铁   12
2  王飞飞   13
"""


#字典创建DataFame   有两个键：'Name' 和 'Age'，它们分别对应着两个值的列表
data4 ={
        'Name':['Tom','Jack','Steve','Ricky'],
        'Age': [28, 34,29, 42]
        }
df4 = pd.DataFrame(data4, index=['score1','score2','score3', 'score4'])
print(df4)
"""
         Name  Age
score1    Tom   28
score2   Jack   34
score3  Steve   29
score4  Ricky   42
"""







