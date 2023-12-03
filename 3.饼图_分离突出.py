
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]

fenli = [0,0,0,0,0,0,0.1,0,0,0]  #将第7块分离出来
plt.pie(amount1,labels=month,autopct='%.1f%%',explode = fenli)
# 总数
# 标签 = 月份
# 百分比值分离=突出

plt.title('就诊人数分布')
