numbers = [12, 37, 5, 42, 8, 3]
even = []
odd=[]
while len(numbers) > 0 :  #循环六次
    number = numbers.pop()
    if(number % 2 == 0):
         even.append(number)
    else:
         odd.append(number)
    
print(number) #列表 numbers 中移除并返回最后一个元素，并将其赋值给变量 number。
#12
#移除了12 ，给了number，次数 numbers就没有12了，只有34,5,42,8,3
print("偶数:",even)
print("奇数:",odd)
