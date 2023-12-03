import numpy as np
data1 = np.array([91, 98.5, 98, 84])# 一维数组

print(data1 [0], data1[3])#91.0 84.0
print(data1[0:2]) #切片不包括右端 [91.  98.5]
print(data1[1:-1])#切片不包括右端 [98.5 98.0 ]

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28,29, 30],
              ])
print(a.shape) # (4,5)  数组形状  行+ 列
print(a.ndim)  # 2 二维数组

b = a.reshape (2,10) #不改变数据的条件下修改形状
print(b, b.shape)
# [[11 12 13 14 15 16 17 18 19 20]
#  [21 22 23 24 25 26 27 28 29 30]] (2, 10)

c = a.reshape (10, 2)
print(c, c.shape)
# [[11 12]
#  [13 14]
#  [15 16]
#  [17 18]
#  [19 20]
#  [21 22]
#  [23 24]
#  [25 26]
#  [27 28]
#  [29 30]]  (10,2) 


t=np.linspace(1,100,10) #等差数列，1-100之间10个元素。包括右端
print(t) #[  1.  12.  23.  34.  45.  56.  67.  78.  89. 100.]


# 创建一个形状为 (height, width) 的全身0的数组
zeros_array = np.zeros((100, 200))
ones_array = np.ones((50, 20))

# 打印数组的形状和数据类型
print("Array shape:", zeros_array.shape) #Array shape: (100, 200)
print("Array data type:", ones_array.dtype) #Array data type: float64

# 创建一个形状为 (height, width) 的空数组
height, width = 100, 200
empty_array = np.empty((height, width))

# 打印数组的形状和数据类型
print("Array shape:", empty_array.shape) #Array shape: (100, 200)
print("Array data type:", empty_array.dtype) #Array data type: float64


