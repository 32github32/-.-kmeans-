import matplotlib.pyplot as plt 
#将matplotlib库中的pyplot模块导入，并为其指定一个简短的别名plt 
import numpy as np  
#将numpy库导入，并为其指定一个简短的别名np
from sklearn.cluster import KMeans
from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
 
iris = datasets.load_iris() 
# SepalLength PetalLength  SepalWidth PetalWidth  Class
#  5.1        3.5          1.4        0.2         Iris-setosa    4+1行
#150列

#——————————————————————————————————————————————————————————————

from sklearn import datasets

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 获取特征数据
X = iris.data

# 获取标签数据
y = iris.target

# 打印数据集信息 （descr 面述信息）
print(iris.DESCR)

"""
    ============== ==== ==== ======= ===== ====================
                    Min  Max   Mean    SD   Class Correlation
    ============== ==== ==== ======= ===== ====================
    sepal length:   4.3  7.9   5.84   0.83    0.7826
    sepal width:    2.0  4.4   3.05   0.43   -0.4194
    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    petal width:    0.1  2.5   1.20  0.76     0.9565  (high!)
    ============== ==== ==== ======= ===== ====================
"""
#————————————————————————————————————————————————————————--
from sklearn import datasets

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 获取特征数据
irisdata = iris.data

# 打印特征数据
print(irisdata)

"""
不要后面的class
[[5.1 3.5 1.4 0.2]
 [4.9 3.0 1.4 0.2]
 [4.7 3.2 1.3 0.2]
 ...
 [6.7 3.0 5.2 2.3]
 [6.3 2.5 5.0 1.9]
 [6.5 3.0 5.2 2.0]]
"""
——————————————————————————————————————————————————————————————————————
import pandas as pd
from sklearn.datasets import load_iris
# 加载鸢尾花数据集
#from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
#iris = datasets.load_iris() 
iris = load_iris()

# 将数据集转化为DataFrame格式
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# 添加目标类别列
df['target'] = iris.target
# 打印前5行数据  head = 5?
print(df.head())

"""

   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target
0                5.1               3.5  ...               0.2       0
1                4.9               3.0  ...               0.2       0
2                4.7               3.2  ...               0.2       0
3                4.6               3.1  ...               0.2       0
4                5.0               3.6  ...               0.2       0

[5 rows x 5 columns]
"""
# 数据集统计摘要
print(df.describe())
"""
       sepal length (cm)  sepal width (cm)  ...  petal width (cm)      target
count         150.000000        150.000000  ...        150.000000  150.000000
mean            5.843333          3.057333  ...          1.199333    1.000000
std             0.828066          0.435866  ...          0.762238    0.819232
min             4.300000          2.000000  ...          0.100000    0.000000
25%             5.100000          2.800000  ...          0.300000    0.000000
50%             5.800000          3.000000  ...          1.300000    1.000000
75%             6.400000          3.300000  ...          1.800000    2.000000
max             7.900000          4.400000  ...          2.500000    2.000000

[8 rows x 5 columns]
"""

# 数据集中各类别的样本数量
print(df['target'].value_counts())
"""
0    50
1    50
2    50
Name: target, dtype: int64
"""
————————————————————————————————————————————————————————————————————————————————————————————-








