
#多元回归 进一步 就是分类  K近邻(k-Nearest Neighbor，KNN)分类


import numpy as np  #  用array数组 必用的包，


#import sklearn   # 要不要都行 
from sklearn.neighbors import KNeighborsClassifier   #K值

#x=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])  #数组
#y=['A','A','B','B']  #数组匹配 集合

#生成训练数据集：
x=np.array ([[4,1,1,2],
             [6,3,3,3],
             [1,1,2,1],
             [2,1,1,1],
             [4,1,1,1],
             [4,2,1,4],
             [4,2,2,2],
             [2,2,1,1],
             [2,1,1.5,1],
             [2,1,0,1]])

y = [160,350,50,50,90,99,100,90,100,38]
#建模：
model = KNeighborsClassifier(n_neighbors=2)
#训练
model.fit(x,y)
#分类：
x_pred = [[3,2,2,3]]  #列向量
y_pred =model.predict(x_pred)  #根据x列向量  去预测y 
print(y_pred)






