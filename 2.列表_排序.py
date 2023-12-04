# 冒泡排序
list = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
length = len(list)
for i in range(length):
    for j in range(length - i):
        if list[length - j - 1] < list[length - j - 2]:
            list[length - j - 1], list[length - j - 2] = list[length - j - 2], list[length - j - 1]
print(list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



