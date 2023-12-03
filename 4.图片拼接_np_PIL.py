import numpy as np
from PIL import Image
# 从 Python Imaging Library（PIL）中导入 Image 类。
# 通过导入 Image 类，可以在 Python 中对图像进行加载、处理和保存等操作。

im1 = np.array(Image.open(r"E:\桌面\新建文件夹\wang (1).png")) #灰度图
im2 = np.array(Image.open(r"E:\桌面\新建文件夹\wang (1) - 副本.png"))

#----------concatenate-----------
im3 = np.concatenate((im1,im2))   #沿0轴拼接，即垂直拼接 = 上下
im3 = Image.fromarray(im3)
im3.show()
im3.save(r"E:\桌面\新建文件夹\wang (上下).png")

im4 = np.concatenate((im1,im2),axis=1) #没1轴拼接，即平行拼接 = 左右
im4 = Image.fromarray(im4)
im4.show()
im4.save(r"E:\桌面\新建文件夹\wang (左右).png")

#-------stack------
im_vstack = np.vstack((im1,im2)) #垂直堆叠
im_hstack = np.hstack((im1,im2)) #水平堆叠
Image.fromarray(im_vstack).save(r"E:\桌面\新建文件夹\wang (垂直堆=上下).png")
Image.fromarray(im_hstack).save(r"E:\桌面\新建文件夹\wang (水平堆=左右).png")


#如果是彩色图像，需要在RGB三个分量上合并后再生成彩色图像保存


