#将最大份额和最小份额从饼图中分离
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]

maxindex = amount1.index(max(amount1))
minindex = amount1.index(min(amount1))

fenli = [0]*len(month)
#fenli = [0,0,0,0,0,0,0.1,0,0,0]  #将第7块分离出来
#创建一个具有 len(month) 个元素的列表 fenli，其中每个元素都是数字 0

fenli[maxindex] = 0.1 #不是0 了 是0.1
fenli[minindex] = 0.1

print(fenli) #[0, 0, 0, 0, 0, 0, 0.1, 0.1, 0, 0]

plt.pie(amount1,labels=month,autopct='%.1f%%',explode = fenli)

plt.title('就诊人数分布')
