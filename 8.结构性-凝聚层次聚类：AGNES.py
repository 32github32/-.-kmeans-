"""
二.结构性聚类(层次聚类)

【树状图！！！】

1.凝聚层次聚类：AGNES算法(自底向上)

首先将每个对象作为一个簇，然后合并这些原子簇为越来越大的簇，直到某个终结条件被满足

2.分裂层次聚类：DIANA算法(自顶向下)

首先将所有对象置于一个簇中，然后逐渐细分为越来越小的簇，直到达到了某个终结条件。

这里我选择的AGNES算法。
"""



from sklearn import datasets     #找鸢尾花？
from sklearn.cluster import AgglomerativeClustering  #AGNES的全称
import matplotlib.pyplot as plt   #画图 
from sklearn.metrics import confusion_matrix #混淆矩阵
import pandas as pd  # Series
# 1 数据
iris = datasets.load_iris()   #加载鸢尾花数据集
irisdata = iris.data    # 不要class列
 # 2 建模
clustering = AgglomerativeClustering(linkage='ward', n_clusters=3)
 # 3 训练
res = clustering.fit(irisdata)
 
# 4 预测？ 
print ("各个簇的样本数目：")

print (pd.Series(clustering.labels_).value_counts())   # counts 计数
"""
各个簇的样本数目：
0    64
1    50
2    36
dtype: int64
"""
print ("聚类结果：")
print (confusion_matrix(iris.target, clustering.labels_))
"""
聚类结果：
[[ 0 50  0]
 [49  0  1]
 [15  0 35]]
"""

# 5 绘图
plt.figure()  #三图合一
#第一张图 x y c
d0 = irisdata[clustering.labels_ == 0]
plt.plot(d0[:, 0], d0[:, 1], 'r.')
#第二张图 x y c
d1 = irisdata[clustering.labels_ == 1]
plt.plot(d1[:, 0], d1[:, 1], 'go')
#第三张图 x y c
d2 = irisdata[clustering.labels_ == 2]
plt.plot(d2[:, 0], d2[:, 1], 'b*')

plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("AGNES Clustering")

plt.show()





















