# 库 → 模块  → 类
# 数据+散点图2
# 建模
# 训练
# 预测
# 散点图2

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
# 和X2 一样 先行在列 例如 (150, 4) 表示X有150行和4列。

# 1.数据 + 绘制数据分布图
plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='see')  
#scatter散点图 plot线图   label就是左上角的 see（第一章图）

plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)   #显示 图例
plt.show()  
#2 建模
estimator = KMeans(n_clusters=3)  # 构造 聚类器
#3 训练
estimator.fit(X)  # 聚类
#4 预测
label_pred = estimator.labels_  # 获取聚类标签

# 5 绘制k-means结果 = 绘图 K = 3
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')  
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')  
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')  
plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)  
plt.show()





