
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 1.数据  （无需测试和训练）
x = [4, 8, 12, 25, 32, 43, 58, 63, 69, 79] #list
y = [20, 33, 50, 56, 42, 31, 33, 46, 65, 75]
x = np.array(x).reshape(len(x), 1) # 转换为列向量  len(x) 行和 1 列
y = np.array(y).reshape(len(y), 1)


# 2.建模
model = LinearRegression()
poly_features = PolynomialFeatures(degree=4)# 设置2、3、4次多项式  
# 创建多项式特征转换器，指定阶数为4  poly = 多

# 3.训练
poly_x = poly_features.fit_transform(x)    # 转换x数据以适合多项式回归模型，自动转换
model.fit(poly_x,y)		# 训练模型

#绘图对比
plt.scatter(x, y,s=50,c = "b") #原始数据散点图 ，画点没画线,s是点的大小,c是颜色

# 4 预测模型折线图     temp它是 "temporary" 的缩写，意为“临时”。
x_temp = np.linspace(0, 80, 100) #横坐标x，由x计算模型输出y
#100像素的意思 ：0 和 80 分别指定了数组的起始值和结束值，而 100 则指定了数组中元素的数量。
#上面的最大值没有超过 80

x_temp = np.array(x_temp).reshape(len(x_temp),1) #横坐标转换为列
poly_x_temp = poly_features.fit_transform(x_temp) 
y_temp = model.predict(poly_x_temp)
#poly_features 对象的 fit_transform 方法，我们可以将原始数据 x_temp 进行多项式特征转换
plt.plot(x_temp, y_temp, 'r')


#自己加一些
plt.xlabel('X label')
plt.ylabel('Y label')
#自己加一些


plt.show()



