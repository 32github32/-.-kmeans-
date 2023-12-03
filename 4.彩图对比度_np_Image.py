from PIL import Image
import numpy as np

# 读取图像
image = Image.open(r"E:\桌面\新建文件夹\OIP-C.jpg")

# 增加对比度的倍数（可以根据需要进行调整）
contrast_multiplier = 1.5

# 将图像转换为numpy数组
image_np = np.array(image)

# 获取图像的行数和列数
rows, cols, channels = image_np.shape

# 遍历图像的每个像素
for i in range(rows):
    for j in range(cols):
        # 获取当前像素的RGB值
        r, g, b = image_np[i, j]

        # 计算新的亮度值
        new_r = (r - 128) * contrast_multiplier + 128
        new_g = (g - 128) * contrast_multiplier + 128
        new_b = (b - 128) * contrast_multiplier + 128

        # 对于超过255的值，设为255
        new_r = min(new_r, 255)
        new_g = min(new_g, 255)
        new_b = min(new_b, 255)

        # 更新像素的RGB值
        image_np[i, j] = [new_r, new_g, new_b]

# 将numpy数组转换回图像
contrasted_image = Image.fromarray(image_np.astype('uint8'))

# 保存增加对比度后的图像
contrasted_image.save(r"E:\桌面\新建文件夹\OIP-Cd对比度.jpg")
