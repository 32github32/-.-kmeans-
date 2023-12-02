
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")
target = 'Class'
ID = 'Code number'

#1.1 生成数据
y = data[target]
data_columns = [x for x in data.columns if x not in [target, ID] ]
x = data[data_columns]

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
[[334   7]
 [  8 175]]
"""
print(confusion_matrix(yTest, yTestPred))
"""
[[114   3]
 [  3  55]]
"""

