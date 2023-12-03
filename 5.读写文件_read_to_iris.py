"""

"""
import pandas as pd

#df = pd.read_csv('hospital.csv')#读文件
#df = pd.read_excel(r'hospital.xlsx')

from sklearn.datasets import load_iris
iris = load_iris()
data1=iris.data

df1 = pd.DataFrame(data1) # 将数据集转化为DataFrame格式
# columns=iris.feature_names 表头，没有的话就没有表头

print(df1) #至显示前五行、后五行
"""
       0    1    2    3
0    5.1  3.5  1.4  0.2
1    4.9  3.0  1.4  0.2
2    4.7  3.2  1.3  0.2
3    4.6  3.1  1.5  0.2
4    5.0  3.6  1.4  0.2
..   ...  ...  ...  ...
145  6.7  3.0  5.2  2.3
146  6.3  2.5  5.0  1.9
147  6.5  3.0  5.2  2.0
148  6.2  3.4  5.4  2.3
149  5.9  3.0  5.1  1.8
"""
print(df1.to_string()) #全部显示：将DataFrame 转换为字符串，并以表格形式打印出来


data=[['张明',10,160],['李铁',22,288],['王飞飞',33,399]]
df2 =pd.DataFrame(data, columns=['name','Age','total'])
print(df2)
"""
  name  Age  total
0   张明   10    160
1   李铁   22    288
2  王飞飞   33    399
"""
#df1.to_csv(r"E:\桌面\新建文件夹\新建文本文档.csv")  #保存文件，没有就会帮我建立
#df2.to_excel (r"E:\桌面\新建文件夹\新建文本文档.xlsx")










  
