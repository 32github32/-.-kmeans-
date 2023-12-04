#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model  #一元也是机器学习  but这是多元线性回归

# 1.数据
x0=[[8,2],[9,0],[11,2],[16,2],[12,0]]   #list的list算作一个变量  
#y0=[[11],[8.5],[15],[18],[11]]  两者都可以
y0=[11,8.5,15,18,11]

x = np.array(x0).reshape(len(x0),2)
y = np.array(y0).reshape(len(y0),1)
#np.array(x0)这部分代码将原始的一维数组 x0 转换成了 NumPy 的数组对象
#.reshape(len(x0), 2) 每行包含两个元素
# x = np.array(x).reshape(len(x), 1) # 转换为列向量  len(x) 行和 1 列

# 2.建模
mymodel = linear_model.LinearRegression();
# 3.训练
mymodel.fit(x,y)
# 4. 预测
x0=[[9,2]] # 9寸、2种辅料
y0=mymodel.predict(x0)

# 输出结果
print('价格为：%.2f'%y0)  #保留小数位 %.2f'%

print(mymodel.coef_) #[[0.84529148 1.96524664]]
#mymodel.coef_ 通常用于获取线性回归模型中各特征的系数a？ 二元有两个？
print(mymodel.intercept_) #[0.87443946]
#mymodel.intercept_ 通常用于获取线性回归模型中的截距项b？
#在一元线性回归模型中，截距就是直线与 y 轴交点的值。
