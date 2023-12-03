
import matplotlib as mpl
import matplotlib.pyplot as plt


month = [1,2,3,4,5,6,7,8,9,10] 
amount1 = [44701, 75661, 75158, 50717, 44987, 57496, 32681, 96430, 62290, 42839]
amount2 = [23255, 11285, 36848, 44526, 33297, 18897, 56314, 76588, 45852, 42401]

#字体
plt.rc('font', family='Arial Unicode MS')


plt.bar(month,amount1,label='一医院')
#x
#y
#底部 = 0
#label
plt.bar(month,amount2,label='二医院',bottom=amount1)
#x
#y
#底部 = amount1
#label
plt.legend()
plt.show()
