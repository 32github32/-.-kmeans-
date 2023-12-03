#4.灰度图垂直上下分割2_np.hstack.py

import numpy as np
from PIL import Image

gray_image = np.array(Image.open(r"E:\桌面\新建文件夹\wang (灰度图).png")) #灰度图

# 假设原始灰度图像为gray_image，其形状为 (height, width)

height, width = gray_image.shape

# 计算每个分割区域的高度
segment_height = height // 3

# 使用切片操作进行垂直分割
segment1 = gray_image[:segment_height, :]
segment2 = gray_image[segment_height:segment_height*2, :]
segment3 = gray_image[segment_height*2:, :]

# 打印每个分割区域的形状
print("Segment 1 shape:", segment1.shape)
print("Segment 2 shape:", segment2.shape)
print("Segment 3 shape:", segment3.shape)

Image.fromarray((segment1)).save(r"E:\桌面\新建文件夹\wang (灰度图4).png")
Image.fromarray((segment2)).save(r"E:\桌面\新建文件夹\wang (灰度图5).png")
Image.fromarray((segment3)).save(r"E:\桌面\新建文件夹\wang (灰度图6).png")

