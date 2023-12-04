#一元线性回归


import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model #多元一样

#1.数据：注意，输入数据必须是array或者dataframe 【和多元一样】
x0=[6,8,10, 14, 18]
y0=[7, 9, 13, 17.5, 18]
x = np.array (x0).reshape (len (x0),1)
y = np.array(y0).reshape(len (y0),1)

#2.建模。建立一元线性回归模型【和多元一样】
mylinearmodel = linear_model.LinearRegression()

#3.训练模型
mylinearmodel.fit(x,y)#x是输入，y是输出，训练模型

#4.预测
a = mylinearmodel.predict([[12]])
print('the price is :%.2f'%a)
print(mylinearmodel.coef_)#x的系数,y=ax+b中的a值
print(mylinearmodel.intercept_)#y轴截距,y=ax+b中的b值
# the price is :13.68
# [[0.9762931]]
# [1.96551724]

#以下为绘图代码

y1 =mylinearmodel.predict(x)
plt.plot(x0,y0,'.')#原始数据
plt.plot(x,y1)
plt.title('Price VS Size')
plt.xlabel('Size')
plt.ylabel('Price')
plt.grid(True)
plt.show()
