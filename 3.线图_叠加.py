from matplotlib import pyplot  as plt
days = range(7)
befor = [6.2, 5.3, 6.1, 7.2, 5.5, 5.8, 5.5]
after = [6.5, 6.4, 7.0, 7.8, 8.5, 8.3, 9.2]

plt.plot(days,befor,label='Before Breakfast')
plt.plot(days,after,label='after Breakfast')
# x
# y
# label

plt.legend(loc='upper right')  #best好一点

