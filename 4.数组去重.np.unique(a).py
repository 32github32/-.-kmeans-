import numpy as np

a = [1,2, 2, 5, 3, 4, 3]  #list  [1, 2, 2, 5, 3, 4, 3]
print('原数组：',a)
b = np.unique(a)  
print('去重后：',b)    #[1 2 3 4 5]



b, indices = np.unique (a, return_index=True)
print('去重：',b)                #列表  去重： [1 2 3 4 5]
print('位置：',indices)          #下标   位置： [0 1 4 5 3]


b,counts = np.unique(a, return_counts=True)
print('去重',b)                    #去重 [1 2 3 4 5]
print('次数',counts)              #次数 [1 2 2 1 1]


c=np.array(['hi','hello','hi','hi','ok']) 
c = np.unique(c)
print(c)                  #['hello' 'hi' 'ok']


