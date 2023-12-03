from PIL import Image
import numpy as np

# 读取图像
image = Image.open(r"E:\桌面\新建文件夹\OIP-C.jpg")

# 增加亮度的值（可以根据需要进行调整）
brightness_increase = 50

# 将图像转换为numpy数组
image_np = np.array(image)

# 获取图像的行数和列数
print(image_np.shape)  #(354, 293, 3)
rows, cols, channels = image_np.shape


# 遍历图像的每个像素
for i in range(rows):
    for j in range(cols):
        # 获取当前像素的RGB值
        r, g, b = image_np[i, j]#将图像数组中指定位置的像素值分别赋值给变量r、g、b。

        # 增加亮度
        r += brightness_increase
        g += brightness_increase
        b += brightness_increase

        # 对于超过255的值，设为255
        r = min(r, 255)
        g = min(g, 255)
        b = min(b, 255)

        # 更新像素的RGB值
        image_np[i, j] = [r, g, b]

# 将numpy数组转换回图像
brightened_image = Image.fromarray(image_np)

# 显示增加亮度后的图像
brightened_image.show()

# 保存增加亮度后的图像
brightened_image.save(r"E:\桌面\新建文件夹\OIP-C1.jpg")

