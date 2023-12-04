
import os  #找文件路径
import pandas as pd

#设置路径
location = r"E:\桌面\课件 (2)"

#空
data = pd.DataFrame ()

#空列表
allfile=[]

for root_dir,sub_dir,files in os.walk(location):
    for filename in files:
        if filename.endswith('xlsx'):
            temp = pd.read_excel(os.path. join(root_dir, filename))
            allfile.append(temp)

#concat 合并
data = pd.concat(allfile)

#保存文件
data.to_excel(location +'/汇总表.xlsx')


