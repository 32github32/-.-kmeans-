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








