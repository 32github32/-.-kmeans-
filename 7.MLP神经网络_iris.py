#MLP 多层感知机模型 深度学习 神经网络

import numpy as np  
import pandas as pd
from sklearn.neural_network import MLPClassifier     #深度学习
from sklearn.model_selection import train_test_split #划分训练集与测试集
from sklearn.metrics import confusion_matrix         #下面又导入一次
from sklearn.metrics import classification_report    #下面又导入一次

# 1.数据
# 1.1 生成数据

from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
iris = datasets.load_iris() 
#from sklearn.datasets import load_iris  #简写


data = pd.DataFrame(data=iris.data, columns=iris.feature_names) #改成dataframe

data['target'] = iris.target  #将 iris 数据集中的 target 列的值赋给了 data 数据集的一个新列
#有iris才这样

#正常情况下：target = 'Class'  #分类目标，2是良性，4是恶性
#           ID = 'Code number'
target1 = 'target'  #!!! 不要方括号。。是将字符串 'target' 赋值给变量 target
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

#print(data['target'].value_counts()) #观察每个分类各有多少个值
#0    50
#1    50
#2    50


#编号code number 和类别 class 两列不做为建模因素，去掉
#编号与结果无关，类别是建模需要计算出来的

newcolumns = [x for x in data.columns if x not in [target1]]  #难  ，或者改为'target'

x = data[newcolumns] #因素
y = data['target']    #实际结果 ,不参加建模 ，但参加结果构成

# 1.2 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x,y)
#x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

# 2. 建立模型 不变
MyMLP = MLPClassifier() 
# MySVC = SVC(kernel = 'rbf') #rbf:高斯核，默认就是rbf


# 3. 训练模型 （训练集去）
MyMLP = MyMLP.fit(x_train, y_train)


# 4. 测试模型，用模型预测分类并与实际的y_test对比 （加上 测试集）
yPred = MyMLP.predict(x_test)  #预测


from sklearn.metrics import classification_report  #分类结果
print(classification_report(y_test, yPred))
#混淆矩阵显示分类结果
"""
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        12
           1       1.00      0.87      0.93        15
           2       0.85      1.00      0.92        11

    accuracy                           0.95        38
   macro avg       0.95      0.96      0.95        38
weighted avg       0.96      0.95      0.95        38
"""
from sklearn.metrics import confusion_matrix
#测试集上的混淆矩阵
print('测试集上的混淆矩阵\n')
print( confusion_matrix( y_test, yPred ) )
"""
测试集test上的混淆矩阵

[[12  0  0]
 [ 0 13  2]
 [ 0  0 11]]
"""
#训练集上的混淆矩阵
print('训练集上的混淆矩阵\n')
y_train_pred = MyMLP.predict(x_train)
print( confusion_matrix( y_train, y_train_pred ))

"""
训练集train上的混淆矩阵

[[38  0  0]
 [ 0 33  2]
 [ 0  0 39]]
"""













