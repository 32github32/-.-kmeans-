import pandas as pd
df=pd.read_csv(r"E:\桌面\课件 (2)\pandas\hospital.csv")#读文件
#print(df)
#数据
#[317 rows x 28 columns]

print(df.to_string())
#看大型数据  list的next  将DataFrame对象转换为字符串并打印出来。

data=[['张明',10,160],
      ['李铁',22,288],
      ['王飞飞',33,399]]

df = pd.DataFrame(data,
                  columns=['name','Age','total'])
df.to_csv(r"E:\桌面\课件 (2)\pandas\三乘三.csv")#保存文件
