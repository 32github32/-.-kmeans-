import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 4., 0.1)

plt.plot(t, t, t, t+2, t, t**2) #线图
#这条语句表示在同一个图形中画出了三条曲线，分别是 (t, t)、(t, t+2) 和 (t, t**2)。

plt.show()
#我是图，我是图，我是图
