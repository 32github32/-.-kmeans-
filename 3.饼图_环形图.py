#环形图
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

plt.pie(amount1, labels=month, radius=1.3,autopct='%1.1f%%', pctdistance=0.9)
# 总数
# 标签=月份
# 半径
# 百分比值
# 百分比值距离
plt.pie(amount2, radius=1,  autopct='%1.1f%%', pctdistance=0.75)

plt.pie([1], radius=0.7, colors='w')

