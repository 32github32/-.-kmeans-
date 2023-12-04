# 利用for输出列表（包括元组，集合等）
A=[1,2,3,4,5]       
for i in A:             # 若元素 i 在列表A里
    print(i)            # 则输出 
# 1
# 2
# 3
# 4
# 5
# 利用for输出数字
for i in range(6,10):   # 若元素 i 在6-10之内，不等于10
    print(i)            # 则输出 i
# 6
# 7
# 8
# 9
# 利用for输出字符串
for i in "I love Chian": # 若字符 i 在字符串内
    print(i)             # 则输出 i    
# l
# o
# v
# e
 
# C
# h
# i
# a
# n
# for还可以和else组合使用
for i in [0,1]:     # 若 i 在【0，1】里
    print(i)        # 则输出 i
else:               # 否则
    print(None)     # 则输出 None
# 0
# 1
# None
# continue跳过当前的循环，执行下个循环
for i in range(5):   #
    if i==3:
        continue
    print("第%d次"%i) #%d是格式化字符串的占位符
# 第0次
# 第1次
# 第2次
# 第4次

# =============================================================================
# range(stop)
# range(start, stop[, step])
# =============================================================================

#步长值输入为2
for i in  range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

# =============================================================================
# for  <变量>   in   <循环序列>:
#        【循环体】
# =============================================================================
# for 循环访问列表
list = ['woodman', 'Alan', 'Bobo']
for name in list:
    print(name)
# woodman
# Alan
# Bobo

# 示例2: for 循环访问字典
dict = {'woodman': 98, 'Alan': 89, 'Bobo': 56}
for key, value in dict.items():
    print(key, value)
# woodman 98
# Alan 89
# Bobo 56

# for 循环访问字符串，可以依次读取每个字符
for char in 'woodman木头人':
    print(char)
# w
# o
# o
# d
# m
# a
# n
# 木
# 头
# 人
for c in 'woodman木头人':
    print(c)
# =============================================================================
# for <外层循环变量> in <外层循环序列>:
#      for <内层循环变量> in <内层循环序列>:
#          【内层循环体】
#      【外层循环体】 
# =============================================================================
for i in range(1, 10): # range()请看本章第五部分
    for j in range(i, 10):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print('')  # 控制换行

# %d * %d = %d 是一个字符串
# % (i, j, i * j) 中，我们传递了一个元组(i, j, i * j)作为参数，按顺序将它们填充到字符串中的占位符中。

# 1 * 1 = 1	1 * 2 = 2	1 * 3 = 3	1 * 4 = 4	1 * 5 = 5	1 * 6 = 6	1 * 7 = 7	1 * 8 = 8	1 * 9 = 9	
# 2 * 2 = 4	2 * 3 = 6	2 * 4 = 8	2 * 5 = 10	2 * 6 = 12	2 * 7 = 14	2 * 8 = 16	2 * 9 = 18	
# 3 * 3 = 9	3 * 4 = 12	3 * 5 = 15	3 * 6 = 18	3 * 7 = 21	3 * 8 = 24	3 * 9 = 27	
# 4 * 4 = 16	4 * 5 = 20	4 * 6 = 24	4 * 7 = 28	4 * 8 = 32	4 * 9 = 36	
# 5 * 5 = 25	5 * 6 = 30	5 * 7 = 35	5 * 8 = 40	5 * 9 = 45	
# 6 * 6 = 36	6 * 7 = 42	6 * 8 = 48	6 * 9 = 54	
# 7 * 7 = 49	7 * 8 = 56	7 * 9 = 63	
# 8 * 8 = 64	8 * 9 = 72	
# 9 * 9 = 81	

# 冒泡排序
list = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
length = len(list)
for i in range(length):
    for j in range(length - i):
        if list[length - j - 1] < list[length - j - 2]:
            list[length - j - 1], list[length - j - 2] = list[length - j - 2], list[length - j - 1]
print(list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list = ['woodman', 'Alan', 'Bobo']
it = iter(list)  # 创建迭代器对象  = 数量大就用迭代器
for name in list:  # 循环访问迭代器
    print(name)
    











