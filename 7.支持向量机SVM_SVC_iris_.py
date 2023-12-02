
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







from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
iris_1 = datasets.load_iris()  #加载鸢尾花数据集，并将其存储在名为 iris_1 的变量中。
data = pd.DataFrame(data=iris_1.data, columns=iris_1.feature_names)
data['target'] = iris_1.target #容易缺
#iris_1.data 包含了鸢尾花数据集的特征数据  导入数据
#iris_1.feature_names 包含了特征的名称  把列导进来 ，后面有data.columns
#通过这行代码将标签数据添加到名为 'target' 的列








#data = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\BreastCancerData.csv")
target1 = 'target'  #分类目标，2是良性，4是恶性
#print(data['Class'].value_counts()) #观察每个分类各有多少个值
#编号和类别两列不做为建模因素，去掉
#编号与结果无关，类别是建模需要计算出来的

newcolumns = [x for x in data.columns if x not in [target1]]  #data上找target1

x = data[newcolumns] #因素
y = data['target']    #实际结果

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

           0       1.00      1.00      1.00        10
           1       0.79      1.00      0.88        11
           2       1.00      0.82      0.90        17

    accuracy                           0.92        38
   macro avg       0.93      0.94      0.93        38
weighted avg       0.94      0.92      0.92        38
"""
from sklearn.metrics import confusion_matrix
#测试集上的混淆矩阵
print('测试集上的混淆矩阵\n')
print( confusion_matrix( y_test, yPred ) )
"""
测试集上的混淆矩阵

[[10  0  0]
 [ 0 11  0]
 [ 0  3 14]]
"""

#训练集上的混淆矩阵
print('训练集上的混淆矩阵\n')
y_train_pred = MySVC.predict(x_train)
print( confusion_matrix( y_train, y_train_pred ))
"""
训练集上的混淆矩阵

[[40  0  0]
 [ 0 39  0]
 [ 0  4 29]]
"""




