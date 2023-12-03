
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
#plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"] #Mac设置支持中文字体
plt.rcParams['axes.unicode_minus'] = False #用于解决负号显示问题的设置

month   = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

x = [ i for i in range(0,len(month))] #横坐标0，1，...，至month的长度
#x不是中点 ，而是开头
#这里的i和下面的i对应
plt.bar(x, amount1,label='一医院',width = 0.4,tick_label=month) #第一个条形图
#x  直接写month，
#Y
#label
#宽度
#用于设置坐标轴刻度标签的参数 刻度和month一样精细

x = [i+0.4 for i in x] #将x向右移bar_width(0.3)
plt.bar(x, amount2,label='二医院',width = 0.4) #第二个条形图,横坐标右移了0.4
#x
#Y
#label
#宽度

plt.title('医院就诊量')
plt.legend(loc='best')
plt.show()







