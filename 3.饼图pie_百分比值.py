
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"] #Mac设置支持中文字体
#plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]

plt.pie(amount1,labels=month,autopct='%.1f%%')
# 总数
# 标签 = 月份
# autopct='%.1f%%'将饼图中每个扇区的百分比值显示为带有一位小数的百分数%形式。

plt.title('就诊人数分布')
plt.show()
