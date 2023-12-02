import matplotlib.pyplot as plt 
#将matplotlib库中的pyplot模块导入，并为其指定一个简短的别名plt 
import numpy as np  
#将numpy库导入，并为其指定一个简短的别名np
from sklearn.cluster import KMeans
from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
 
iris = datasets.load_iris() 
# SepalLength PetalLength SepalWidth PetalWidth Class
#5.1 3.5  1.4 0.2 Iris-setosa    4+1行
#150列

X = iris.data[:, :4]  # #表示我们取特征空间中的4个维度
#切片 和X2 一样 先行在列

print(X.shape)   # (150, 4)
# 和X2 一样 先行在列




