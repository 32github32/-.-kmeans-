from matplotlib import pyplot  as plt

stu_height = {
    '张天玲':175,
    '李铁':178,
    '王玉玨':173,
    '黄鸿':172,
    '赵强':176,
    '李文顶':175,
    '覃飞':180,
    '苏决':168,
    '钱前':179
}
stu_selected = {}
for name, height in stu_height.items():
    if height >= 175:
        stu_selected[name] = height

print(stu_selected)
#{'张天玲': 175, '李铁': 178, '赵强': 176, '李文顶': 175, '覃飞': 180, '钱前': 179}

#字典转列表
names = list(stu_selected.keys())
StuHeights = list(stu_selected.values())

#字体
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]

#画图x y
plt.plot(names,StuHeights)
plt.xlabel('姓名')
plt.ylabel('身高')
plt.title('学生身高情况')
plt.grid(visible='True')

for name in names:
    plt.text(name, #名字
             StuHeights[ names.index(name) ],#身高
             str(name)+str(StuHeights[ names.index(name) ]))#格式
plt.show()








