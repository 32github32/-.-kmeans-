import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
#plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"] #Mac设置支持中文字体
#plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
#amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

plt.bar(month, amount1,label='一医院', width=0.6)
# X  、Y 、  便签 、 宽度

plt.title('第一医院就诊量')
plt.xlabel('月份')
plt.ylabel('就诊人数')
plt.legend(loc='upper right') #没有不行


for i in range(0,len(month)):  #len(month) =10
    plt.text(month[i]-0.3,amount1[i],str(amount1[i]))
    #文本在哪？ x方向、y方向、字符串
plt.show()

