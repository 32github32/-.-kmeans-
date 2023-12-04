 #1.\ （在行尾时）- 续行符

a = '<我是第1行的内容>\
     <我是第2行的内容>\
     <我是第3行的内容>\
     <我是第4行的内容>' 
print(a)  # <我是第1行的内容><我是第2行的内容><我是第3行的内容><我是第4行的内容>


#1.\n - 换行
print("<我是第1行的内容>\n<我是第2行的内容>\n<我是第3行的内容>\n<我是第4行的内容>") 

#1.\\ - 反斜杠符号

print("Hello\\World")  # Hello\World

#1.\' - 单引号

print("What\'s your name?") # What's your name?

#1.\" - 双引号
print("\"Hello World\"")  # "Hello World"

#1.程序员的小快乐——\a
a = 'Hello world!\a' 
print(a) #Hello world!  #响铃 ^BELL^

#1.\b - 退格
print("Hello World\b")  # Hello Worl
print("Hello World\b\b\b\b\bDevil Ding")  # Hello Devil Ding

#1.\0 / \000 - 空字符
print(len("Hello World") )  # 11 
print(len("Hello World\0") )  # 12 
print("Hello World\000") 
print("Hello World\0000")  # 结果如下图所示


#1.\t - 横向制表符
print("Hello\n\tWorld")
# Hello
# 	World

#1.\r - 回车
#\r (return) 指回到本行行首，\n (new line) 指开启新的一行。
print("Hello", end="")  #Hello
print("\r", end="") 
print("World!", end="")  

print("over\r") 
# print("\nover")  

# print("Hello", end="") 
# print("\n", end="") 
# print("World", end="")

#1.


#1.
