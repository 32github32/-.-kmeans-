import matplotlib.pyplot as plt
import numpy as np

# 生成一些随机数据
x = np.random.rand(100)
y = np.random.rand(100)
z = x + y  # 计算数据点的和

# 绘制散点图
plt.scatter(x, y, s=z*1000, c=z)  # #原始数据散点图 ，画点没画线,s是点的大小,c是颜色
#
# 设置横纵坐标轴标签
plt.xlabel('X label')
plt.ylabel('Y label')

# 显示图像
plt.show()

"""
s：指定散点的大小。
c：指定散点的颜色。
marker：指定散点的形状。
alpha：指定散点的透明度。
linewidths：指定散点边缘的线条宽度。
edgecolors：指定散点边缘的颜色。
"""


"""
matplotlib库中，当你绘制图表时可以使用marker参数来指定数据点的标记样式。
marker参数有很多不同的取值，下面是一些常用的marker参数及其含义：

. : 点标记
, : 像素标记
o : 圆圈标记
v : 倒三角标记
^ : 三角标记
< : 左三角标记
> : 右三角标记
s : 正方形标记
p : 五边形标记
* : 星形标记
+ : 加号标记
x : X形标记

你还可以通过以下方法设置标记的其他属性：

markeredgecolor：标记边缘的颜色
markeredgewidth：标记边缘的宽度
markerfacecolor：标记内部的颜色
markersize：标记的大小
例如，在使用matplotlib绘制散点图时，你可以这样设置marker的参数：


python

import matplotlib.pyplot as plt

plt.scatter(x, y, marker='o', c='b', s=50, label='Data points')
plt.show()


在这个例子中，我们使用了marker='o'来指定数据点的标记为圆圈，c='b'指定颜色为蓝色，s=50指定标记的大小为50。size？
"""










