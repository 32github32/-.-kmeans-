# 冒泡排序
list = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
length = len(list)
for i in range(length):
    for j in range(length - i):
        if list[length - j - 1] < list[length - j - 2]:
            list[length - j - 1], list[length - j - 2] = list[length - j - 2], list[length - j - 1]
print(list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#————————————————————————————————————————————————————————————————————————————


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
#或者 a = my_list.sort()
print(my_list)  # 输出: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#不可以 a = my_list.sort()

#————————————————————————————————————————————————————————————————————————————
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list)
print(sorted_list)  # 输出: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

