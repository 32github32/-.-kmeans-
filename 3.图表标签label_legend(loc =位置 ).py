"""
传说，传奇故事；传奇人物；（标志、徽记、硬币等物品上的）刻印文字，铭文；（图片或地图的）文字说明，图例

在 Matplotlib 中，plt.legend() 函数用于显示图例，而 loc 参数用于指定图例的位置。具体来说，plt.legend(loc=2) 中的 loc=2 表示将图例放置在图的左上角。

Matplotlib 中 plt.legend() 函数的 loc 参数可以取不同的值来指定图例的位置，常见的取值包括：

0: 'best'，自动选择最佳位置。
1: 'upper right'，右上角。
2: 'upper left'，左上角。
3: 'lower left'，左下角。
4: 'lower right'，右下角。
5: 'right'，右侧。
6: 'center left'，左侧中间。
7: 'center right'，右侧中间。
8: 'lower center'，底部中间。
9: 'upper center'，顶部中间。
10: 'center'，正中间。
因此，当你使用 plt.legend(loc=2) 时，表示你希望将图例放置在图的左上角。当然，你也可以根据需要选择其他位置来放置图例。
"""





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
plt.show()






