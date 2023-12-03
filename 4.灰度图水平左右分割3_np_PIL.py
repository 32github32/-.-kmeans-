#4.灰度图水平左右分割3_np_PIL.py

import numpy as np
from PIL import Image

gray_image = np.array(Image.open(r"E:\桌面\新建文件夹\wang (灰度图).png")) #灰度图

# 假设原始灰度图像为gray_image，其形状为 (height, width)
height, width = gray_image.shape

# 计算每个分割区域的宽度
segment_width = width // 3  #宽度除3

# 使用切片操作进行水平分割 = 数组
segment1 = gray_image[:, :segment_width]
segment2 = gray_image[:, segment_width:segment_width*2]
segment3 = gray_image[:, segment_width*2:]

# 打印每个分割区域的形状
print("Segment 1 shape:", segment1.shape)
print("Segment 2 shape:", segment2.shape)
print("Segment 3 shape:", segment3.shape)

#数组转图片
Image.fromarray((segment1)).save(r"E:\桌面\新建文件夹\wang (灰度图7).png")
Image.fromarray((segment2)).save(r"E:\桌面\新建文件夹\wang (灰度图8).png")
Image.fromarray((segment3)).save(r"E:\桌面\新建文件夹\wang (灰度图9).png")
