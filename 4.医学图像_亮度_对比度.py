#做不出来


import PIL.ImageShow
from PIL import Image
import numpy as np

#im = np.array(Image.open('CTExample.jpg').convert('L')) #转灰度图
#Image.fromarray(im).save('原照片.jpg')
im = np.array(Image.open('原照片.jpg'))
print(im.shape)
# (787, 1300)

#调亮,增加亮度
row, col = im.shape

newim1 = np.empty([1,row*col], dtype=im.dtype) #只有一行
diff = 50
i=0
for element in im.flat: #flat: 数组元素迭代
    newim1[0,i] = min(255, element + diff)
    i = i+1

newim1 = newim1.reshape([row, col]) #转换成2维图片
Image.fromarray(newim1).save('增加亮度.jpg')
newim1.show()
#PIL.ImageShow.show(Image.fromarray(newim1))
# 增加对比度(对比度是最白与最黑亮度单位的相除值。因此白色越亮、黑色越暗，对比度就越高。)
newim2 = np.zeros([row,col], dtype=im.dtype)
for i in np.arange(im.shape[0]):
    for j in np.arange(im.shape[1]):
        if im[i,j]>125:
            newim2[i,j] = min(im[i,j]+100,255) #增加亮度不能超过255
        else:
            newim2[i,j] = max(im[i,j]-50, 0)  #降低亮度，不低于0
Image.fromarray(newim2).save('增加对比度.jpg')
