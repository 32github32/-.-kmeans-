from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
iris_1 = datasets.load_iris()  #加载鸢尾花数据集，并将其存储在名为 iris_1 的变量中。
data = pd.DataFrame(data=iris_1.data, columns=iris_1.feature_names)
data['target'] = iris_1.target 
target1 = 'target'
#data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")
#target = 'Class'
#ID = 'Code number'

#1.1 生成数据

data_columns = [x for x in data.columns if x not in [target1] ]
x = data[data_columns]
y = data[target1]  #上面X不要data.target1 ，Y要

# 1.2 划分训练集和测试集 XXYY 
xTrain, xTest, yTrain, yTest = train_test_split(x, y) 
# 2 建模
NewModel = LogisticRegression()
# 3 训练
NewModel = NewModel.fit(xTrain,yTrain)
# 4 预测
yTrainPred = NewModel.predict(xTrain)
yTestPred = NewModel.predict(xTest)

print(confusion_matrix(yTrain, yTrainPred))
"""
[[40  0  0]
 [ 0 35  3]
 [ 0  1 33]]
"""
print(confusion_matrix(yTest, yTestPred))
"""
[[10  0  0]
 [ 0 12  0]
 [ 0  0 16]]
"""


