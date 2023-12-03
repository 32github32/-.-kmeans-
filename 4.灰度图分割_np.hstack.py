import numpy as np
from PIL import Image

im = np.array(Image.open(r"E:\桌面\新建文件夹\wang (灰度图).png")) #灰度图

print(im.shape) #(245, 361)
row, col = im.shape
#分割成3行、2列共6幅图像
#偶数列才能水平均匀分割成2个,　3的倍数行才能垂直均匀分割成3个
if col%2 == 1: 
    #奇数列  col除以2的余数是否等于1    3  5 7 9 
    temp = np.zeros([row,1],dtype=im.dtype)
    #np.zeros() 是 NumPy 库中用于创建指定形状的全零数组的函数。
    #[row, 1] 指定了数组的形状，这里是一个二维数组，行数为 row，列数为 1。
    #dtype=im.dtype 指定了数组的数据类型与变量 im 的数据类型一致。
    im = np.hstack((im, temp)) 
    #增加1列变成2的倍数列
    #im = 数组图
    #奇数列图
    #im = im[:,0:col-1] #也可以去掉最后一列
    
row, col = im.shape
if row%3 !=0:
    #row除以3的余数是否不等于0
    temp = np.zeros([3-row%3, col],dtype=im.dtype)
    im = np.vstack((im, temp)) #增加row%3行，变成3的倍数行

im_hslipt2 = np.hsplit(im,2) 
#水平分割数组  得到b[0], b[1]两个，分别是左一半和右一半
#只能分隔成两个

Image.fromarray((im_hslipt2[0])).save(r"E:\桌面\新建文件夹\wang (灰度图1).png")
Image.fromarray((im_hslipt2[1])).save(r"E:\桌面\新建文件夹\wang (灰度图2).png")




