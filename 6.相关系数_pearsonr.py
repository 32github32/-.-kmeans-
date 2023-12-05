import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

import statsmodels.api as sm
from scipy.stats.stats import pearsonr


#新增加的两行
import matplotlib
matplotlib.rc("font",family='YouYuan')

# 1.1输数据
df = pd.DataFrame([[2.3,3.90],
                   [2.2,3.81],
                   [2.8,4.62],
                   [2.6,4.72],
                   [2.9,5.10],
                   [3.3,5.08],
                   [3.6,5.10],
                   [3.1,5.03],
                   [3.7,5.20],
                   [3.8,5.24],
                   [3.5,5.83],
                   [4.0,6.12]],
                  columns=['直径','树高'])
print(df)    

# 1.2绘图  
p_X=df['直径']
p_Y=df['树高']
plt.figure(figsize=(10, 5))
plt.scatter(p_X,p_Y,color='b',label='data')
plt.xlabel('直径')
plt.ylabel('树高')
plt.show()   

# 3.相关系数
r=pearsonr(df['直径'],df['树高'])[0]
print('相关系数r：',r) #相关系数r： 0.8879822122271797


r1 = df.corr()
print(r1)
#           直径        树高
# 直径  1.000000  0.887982
# 树高  0.887982  1.000000

"""
X=df['直径']                #自变量
X=sm.add_constant(X)        #自变量做一些处理
model=sm.OLS(df['树高'],X)  #sm.OLS 直线回归的函数
model = model.fit()         #fit 适配  拟合
model.summary()
model.params
"""



