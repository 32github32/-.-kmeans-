"""

"""
import pandas as pd
df1 = pd.read_excel (r"E:\桌面\新建文件夹\新建文本文档.xlsx",
                     sheet_name=0, #第一个sheet1
                     header=1)      
#默认header=0，即第0行为列标签
#设置header=i，则第i行为列标签，i行之前全部清除
print(df1)
"""
   0   张明  10  160
0  1   李铁  22  288
1  2  王飞飞  33  399
"""




"""
读列
df1 = pd.read_excel(r'hospital.xlsx',usecols=[1])
df2 = pd.read_excel(r'hospital.xlsx',usecols=[1,2])
df3 = pd.read_excel(r'hospital.xlsx',usecols=['医院名称',
                                              '季度’，
                                              ‘业务总收入（万元）‘]）
读行
df4 = pd.read_excel (r'hospital.xlsx',nrows=4)    
跳行
df4 = pd.read_excel (r'hospital.xlsx',skiprows=[1,3]) #跳过1,3行       
"""









  
