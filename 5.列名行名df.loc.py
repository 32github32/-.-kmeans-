"""

"""
import pandas as pd

data=[['张明',10,160],
      ['李铁',22,288],
      ['王飞飞',33,399]]

df = pd.DataFrame(data, 
                  columns=['name','Age','total'],  #多list自己取列名
                  index=[2201, 2202, 2203])        #都可以设行名

data1=df.loc[:,'total']  #所有行,total列
#df.loc[行名]，df.loc[行名，列名]，：取行，显式索引
print(data1)
"""
2201    160
2202    288
2203    399
Name: total, dtype: int64
"""
data2 = df. loc[ [2201,2203],['name', 'total']]
print(data2)
"""
     name  total
2201   张明    160
2203  王飞飞    399
"""
data3 = df['Age']  #df[列名]：取列
print(data3)
"""
     name  total
2201   张明    160
2203  王飞飞    399
"""




  
