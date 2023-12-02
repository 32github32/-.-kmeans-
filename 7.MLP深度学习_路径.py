#MLP 多层感知机模型 深度学习 神经网络

import numpy as np  
import pandas as pd
from sklearn.neural_network import MLPClassifier     #深度学习
from sklearn.model_selection import train_test_split #划分训练集与测试集
from sklearn.metrics import confusion_matrix         #下面又导入一次
from sklearn.metrics import classification_report    #下面又导入一次

# 1.数据
# 1.1 生成数据
data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")

"""
Code number	Clump Thickness	Uniformity of Cell Size	Uniformity of Cell Shape	Marginal Adhesion	Single Epithelial Cell Size	Bare Nuclei	Bland Chromatin	Normal Nucleoli	Mitoses	Class
1000025	5	1	1	1	2	1	3	1	1	2
1002945	5	4	4	5	7	10	3	2	1	2

"""
target = 'Class'  #分类目标，2是良性，4是恶性
ID = 'Code number'

print(data['Class'].value_counts()) #观察每个分类各有多少个值
#2    458
#4    241


#编号code number 和类别 class 两列不做为建模因素，去掉
#编号与结果无关，类别是建模需要计算出来的

newcolumns = [x for x in data.columns if x not in [target, ID]]

x = data[newcolumns] #因素
y = data['Class']    #实际结果 ,不参加建模 ，但参加结果构成

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
ame: Class, dtype: int64
              precision    recall  f1-score   support

           2       0.98      0.94      0.96       120
           4       0.88      0.96      0.92        55

    accuracy                           0.95       175
   macro avg       0.93      0.95      0.94       175
weighted avg       0.95      0.95      0.95       175
"""
from sklearn.metrics import confusion_matrix
#测试集上的混淆矩阵
print('测试集上的混淆矩阵\n')
print( confusion_matrix( y_test, yPred ) )
"""
测试集test上的混淆矩阵

[[113   7]
 [  2  53]]
"""
#训练集上的混淆矩阵
print('训练集上的混淆矩阵\n')
y_train_pred = MyMLP.predict(x_train)
print( confusion_matrix( y_train, y_train_pred ))

"""
训练集train上的混淆矩阵

[[334   4]
 [  4 182]]
"""
