

import pandas as pd
data=[['张明',10,160],['李铁',22,288],['王飞飞',33,399]]
df = pd. DataFrame (data, columns=['name','Age','total' ])
print(df)
#   name  Age  total
# 0   张明   10    160
# 1   李铁   22    288
# 2  王飞飞   33    399

names=df['name'] #取name列,结果是series
print(names)
# 0     张明   【这是Series】
# 1     李铁
# 2    王飞飞
#Name: name, dtype: object


score=list(df['total'])#取total列,结果是list ,因为我写了list
print(score)

#[160, 288, 399]
