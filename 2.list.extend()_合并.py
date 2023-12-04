my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)  # 输出: [1, 2, 3, 4, 5, 6]


my_list = [1, 2, 3]
a=[4]
my_list.extend(a)
print(my_list)  # 输出: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_list.extend(my_tuple)
print(my_list)  # 输出: [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3]
my_str = "hello"
my_list.extend(my_str)
print(my_list)  # 输出: [1, 2, 3, 'h', 'e', 'l', 'l', 'o']


