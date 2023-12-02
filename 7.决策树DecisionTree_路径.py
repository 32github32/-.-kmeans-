import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree #从 Scikit-learn 库中导入决策树算法的模块 tree
from sklearn.model_selection import train_test_split #划分训练集与测试集

# 1.数据
# 1.1 生成数据
data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")

target = 'Class'  #分类目标，2是良性，4是恶性
ID = 'Code number'

#print(data['Class'].value_counts()) #观察每个分类各有多少个值

#编号和类别两列不做为建模因素，去掉
#编号与结果无关，类别是建模需要计算出来的

newcolumns = [x for x in data.columns if x not in [target, ID]]

x = data[newcolumns] #因素
y = data['Class']    #实际结果

# 1.2 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x,y)
#x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

# 2. 建立模型
myDecisionTree = tree.DecisionTreeClassifier()
# 3. 训练模型
myDecisionTree = myDecisionTree.fit(x_train, y_train)
# 4. 测试模型，用模型预测分类并与实际的y_test对比
yPred = myDecisionTree.predict(x_test)  #预测

from sklearn.metrics import classification_report
print(classification_report(y_test, yPred))
#混淆矩阵显示分类结果
"""
              precision    recall  f1-score   support

           2       0.93      0.96      0.95       113
           4       0.93      0.87      0.90        62

    accuracy                           0.93       175
   macro avg       0.93      0.92      0.92       175
weighted avg       0.93      0.93      0.93       175
"""
from sklearn.metrics import confusion_matrix
#测试集上的混淆矩阵
print('测试集上的混淆矩阵\n')

print( confusion_matrix( y_test, yPred ) )
"""
测试集上的混淆矩阵

[[109   4]
 [  8  54]]
"""
#训练集上的混淆矩阵
print('训练集上的混淆矩阵\n')
y_train_pred = myDecisionTree.predict(x_train)
print( confusion_matrix( y_train, y_train_pred ))
"""
训练集上的混淆矩阵

[[345   0]
 [  0 179]]
"""


