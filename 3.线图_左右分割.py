# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

#字体
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
#plt.rcParams['axes.unicode_minus'] = False

#数据
month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]


plt.subplot(121)
# 第一个参数 1 表示将整个绘图区域分割成1行。
# 第二个参数 2 表示将整个绘图区域分割成2列。
# 最后一个参数 1 表示当前选中的子图的索引，即在1行2列的网格中选择第1个子图（从左到右，从上到下编号）。
plt.plot(month, amount1,color="r", linestyle=":", marker="s")
# x
# y
# 颜色
# 风格
# 点式

plt.subplot(122)
plt.plot(month, amount2,color="b", linestyle="-", marker="o")

plt.show()


