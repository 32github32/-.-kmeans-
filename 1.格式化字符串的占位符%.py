# continue跳过当前的循环，执行下个循环
for i in range(5):
    if i==3:
        continue
    print("第%d次"%i) #%d是格式化字符串的占位符
# 第0次
# 第1次
# 第2次
# 第4次
# 将整数i插入到字符串中


i = 3
print("第%d次" % i) #第3次

# 将浮点数f插入到字符串中
f = 1.23
print("浮点数为%.2f" % f) #浮点数为1.23

# 将字符串s插入到字符串中
s = "hello"
print("字符串为%s" % s) #字符串为hello
