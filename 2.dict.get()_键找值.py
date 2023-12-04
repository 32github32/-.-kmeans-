my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 使用 get() 方法获取指定键的值
name = my_dict.get("name")
print("姓名:", name)

# 指定默认值
gender = my_dict.get("gender", "Unknown")
print("性别:", gender)


#姓名: Alice
#性别: Unknown
