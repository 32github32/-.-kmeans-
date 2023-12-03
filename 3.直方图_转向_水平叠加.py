#-*-coding：utf-8-*-

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

plt.barh(month,amount1,label='一医院')
plt.barh(month,amount2,label='二医院',left=amount1)
#y
#x
#label
#不是butter 而是 left 

plt.xlabel('就诊人数')
plt.ylabel('月份')
plt.legend(loc='best')
