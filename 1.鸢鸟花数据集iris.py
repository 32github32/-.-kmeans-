import matplotlib.pyplot as plt 
#将matplotlib库中的pyplot模块导入，并为其指定一个简短的别名plt 
import numpy as np  
#将numpy库导入，并为其指定一个简短的别名np
from sklearn.cluster import KMeans
from sklearn import datasets    #为了导入 iris 鸢鸟花数据集
 
iris = datasets.load_iris() 
# SepalLength PetalLength SepalWidth PetalWidth Class
#5.1 3.5  1.4 0.2 Iris-setosa    4+1行
#150列



from sklearn import datasets

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 获取特征数据
X = iris.data

# 获取标签数据
y = iris.target

# 打印数据集信息
print(iris.DESCR)
