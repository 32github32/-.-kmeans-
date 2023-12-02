"""
二.结构性聚类(层次聚类)
1.凝聚层次聚类：AGNES算法(自底向上)

首先将每个对象作为一个簇，然后合并这些原子簇为越来越大的簇，直到某个终结条件被满足

2.分裂层次聚类：DIANA算法(自顶向下)

首先将所有对象置于一个簇中，然后逐渐细分为越来越小的簇，直到达到了某个终结条件。

这里我选择的AGNES算法。
"""



from sklearn import datasets
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pandas as pd
 
iris = datasets.load_iris()
irisdata = iris.data
 
clustering = AgglomerativeClustering(linkage='ward', n_clusters=3)
 
res = clustering.fit(irisdata)
 
print ("各个簇的样本数目：")
print (pd.Series(clustering.labels_).value_counts())
print ("聚类结果：")
print (confusion_matrix(iris.target, clustering.labels_))
 
plt.figure()
d0 = irisdata[clustering.labels_ == 0]
plt.plot(d0[:, 0], d0[:, 1], 'r.')
d1 = irisdata[clustering.labels_ == 1]
plt.plot(d1[:, 0], d1[:, 1], 'go')
d2 = irisdata[clustering.labels_ == 2]
plt.plot(d2[:, 0], d2[:, 1], 'b*')
plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("AGNES Clustering")
plt.show()






















