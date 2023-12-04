import pandas as pd
df2 = pd.read_excel(r'E:\桌面\课件 (2)\老师给的代码\hospital.xlsx',usecols=[1,2])
print(df2)


#def read(encoding='utf-8'):  不要这个。这个有毒。
#要就要缩减4格
#-*- coding:utf-8 -*-
#义一个函数的语法。这个函数名为read，它接受一个参数encoding，默认值为'utf-8'。

#读文件 
#df1 = pd.read_csv(r'E:\桌面\课件 (2)\老师给的代码\hospital.csv',usecols=[1])





"""
只能一个一个文件的读

import pandas as pd
df1 = pd.read_excel (r"E:\桌面\新建文件夹\新建文本文档.xlsx",
                     sheet_name=0, #第一个sheet1
                     header=1)      
#默认header=0，即第0行为列标签
#设置header=i，则第i行为列标签，i行之前全部清除
print(df1)

   0   张明  10  160
0  1   李铁  22  288
1  2  王飞飞  33  399
"""




"""
import pandas as pd
#def read(encoding='utf-8'):  不要这个。这个有毒。
#要就要缩减4格
#-*- coding:utf-8 -*-
#义一个函数的语法。这个函数名为read，它接受一个参数encoding，默认值为'utf-8'。

#读文件 
#df1 = pd.read_csv(r'E:\桌面\课件 (2)\老师给的代码\hospital.csv',usecols=[1])

df2 = pd.read_excel(r'E:\桌面\课件 (2)\老师给的代码\hospital.xlsx',usecols=[1,2])
print(df2)
#     df3 = pd.read_excel(r'hospital.xlsx',usecols=['医院名称',
#                                                   '季度',
#                                                   '业务总收入（万元）'])
# #读行
#     df4 = pd.read_excel (r'hospital.xlsx',nrows=4)    
# #跳行
#     df4 = pd.read_excel (r'hospital.xlsx',skiprows=[1,3]) #跳过1,3行      




#     df0 = pd.read_csv(r"E:\桌面\课件 (2)\老师给的代码\hospital.csv")
# #wdir很可能是一个变量名，它通常用来表示"working directory"（工作目录）的缩写。
# #如果您在运行器中只看到 "runfile wdir"，可能是因为Spyder无法正确获取要运行的文件的路径。

#     df1 = pd.read_excel(r'E:\桌面\课件 (2)\pandas\hospital.xlsx',usecols=[1])

#     df2 = pd.read_excel(r'E:\桌面\课件 (2)\pandas\hospital.xlsx',usecols=[1,2])

#     df3 = pd.read_excel(r'E:\桌面\课件 (2)\pandas\hospital.xlsx',
#                     usecols=['医院名称','季度','业务总收入（万元）'])
               

#     df4 = pd.read_excel(r'E:\桌面\课件 (2)\pandas\hospital.xlsx',nrows=4)


   
"""









  
