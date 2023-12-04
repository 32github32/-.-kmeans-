# -*- coding:utf-8 -*-.

#-*-coding：utf-8-*-

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

#import matplotlib
#matplotlib.rc("font",family='YouYuan')
#使用plt.rcParams设置了字体和图表大小
#plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

plt.bar(month, amount1,label='一医院') #bar=直方图
plt.title('第一医院就诊量')
plt.xlabel('月份')
plt.ylabel('就诊人数')

#plt.show() 要不要都行
