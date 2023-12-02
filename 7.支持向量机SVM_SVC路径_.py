
import numpy as np
import pandas as pd
from sklearn.svm import SVC
"""
SVM=Support Vector Machine 是支持向量
SVC=Support Vector Classification就是支持向量机用于分类，
SVC=Support Vector Regression.就是支持向量机用于回归分析
"""
from sklearn.model_selection import train_test_split  #划分训练集与测试集 

from sklearn.metrics import classification_report  #  "metrics" 是指度量或评估指标
from sklearn.metrics import confusion_matrix   #混淆矩阵 “Matrix” 是指矩阵

# 1.数据
# 1.1 生成数据
data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")

target1 = 'Class'  #分类目标，2是良性，4是恶性
ID2 = 'Code number'

#print(data['Class'].value_counts()) #观察每个分类各有多少个值

#编号和类别两列不做为建模因素，去掉
#编号与结果无关，类别是建模需要计算出来的

newcolumns = [x for x in data.columns if x not in [target1, ID2]]

x = data[newcolumns] #因素
y = data['Class']    #实际结果

# 1.2 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x,y)  #  XX  YY
#x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

# 2. 建立模型 :核函数 映射到高维空间
MySVC = SVC()
# MySVC = SVC(kernel = 'rbf') #rbf:高斯核，默认就是rbf
#线性核
#多项式核


# 3. 训练模型
MySVC = MySVC.fit(x_train, y_train)   #变量变换
# 4. 测试模型，用模型预测分类并与实际的y_test对比
yPred = MySVC.predict(x_test)  #预测

from sklearn.metrics import classification_report
print(classification_report(y_test, yPred))
#混淆矩阵显示分类结果
"""
              precision    recall  f1-score   support

           2       0.99      0.96      0.97       117
           4       0.92      0.98      0.95        58

    accuracy                           0.97       175
   macro avg       0.96      0.97      0.96       175
weighted avg       0.97      0.97      0.97       175
"""
from sklearn.metrics import confusion_matrix
#测试集上的混淆矩阵
print('测试集上的混淆矩阵\n')
print( confusion_matrix( y_test, yPred ) )
"""
测试集上的混淆矩阵

[[112   5]
 [  1  57]]
"""

#训练集上的混淆矩阵
print('训练集上的混淆矩阵\n')
y_train_pred = MySVC.predict(x_train)
print( confusion_matrix( y_train, y_train_pred ))
"""
训练集上的混淆矩阵

[[334   7]
 [  3 180]]
"""




