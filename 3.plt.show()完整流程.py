import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 绘制线图
plt.plot(x, y)

# 添加标题和标签
plt.title("My First Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 显示图表
plt.show()


#最简单的matplotlib.pyplot 使用方法： 数据 + 线图（这步已经有图了） +  标签题目  +  显示
——————————————————————————————————————————————————————————————————————————————————————————

# 5 绘图
plt.figure()  #三图合一

#第一张图 x y c
d0 = irisdata[clustering.labels_ == 0]  
plt.plot(d0[:, 0], d0[:, 1], 'r.')

#第二张图 x y c
d1 = irisdata[clustering.labels_ == 1]
plt.plot(d1[:, 0], d1[:, 1], 'go')

#第三张图 x y c
d2 = irisdata[clustering.labels_ == 2]
plt.plot(d2[:, 0], d2[:, 1], 'b*')

plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("AGNES Clustering")

plt.show()
——————————————————————————————————————————————————————————————————————————————————————————
