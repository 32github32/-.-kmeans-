import matplotlib.pyplot as plt    # 画图
import numpy as np             # ？
from sklearn.cluster import KMeans  #聚类 K-means
from sklearn import datasets   # iris
from  sklearn.cluster import DBSCAN  
# sklearn 是 scikit-learn 库的顶层包，提供了许多用于机器学习和数据挖掘的工具。
# 而 sklearn.cluster 则是 scikit-learn 库中专门用于聚类分析的模块
 
iris = datasets.load_iris()   # 加载 iris 
X = iris.data[:, :4]          # 表示我们只取特征空间中的4个维度  不要class
print(X.shape)                #(150, 4)
# 绘制数据分布图 【总图】
plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='see')  
plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)  
plt.show()  

# 2 建模
dbscan = DBSCAN(eps=0.4, min_samples=9)
#两个样本之间的最大距离为 0.4，一个核心点所需的最小样本数量为 9

# 3 训练
dbscan.fit(X)   
#X = iris.data[:, :4]  

#4 预测
label_pred = dbscan.labels_  #固定？
 #print(dbscan.labels_)  输出可能如下所示：[0 0 0 1 1 -1] 分为三簇
 
 
# 绘制k-means结果
# plt.figure()  # 要不要都行

#分为三簇
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

















