import pandas as pd

# 创建一个 DataFrame 对象
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Math': [85, 90, 78, 60],
        'English': [70, 80, 75, 65]}
df = pd.DataFrame(data)
print(df)
"""
      Name  Math  English
0    Alice    85       70
1      Bob    90       80
2  Charlie    78       75
3    David    60       65
"""

# 计算平均成绩
df['Average'] = df[['Math', 'English']].mean(axis=1) #增加了average项
#axis=1 表示对 DataFrame 进行沿着列方向的操作  垂直
#axis=0 表示对 DataFrame 进行沿着行方向的操作  水平
#.mean(axis=1) 表示对选定的两列沿着行的方向进行求平均值的操作。


# 筛选出不及格的学生
failures = df[df['Average'] < 70]

print(df)
"""
      Name  Math  English  Average
0    Alice    85       70     77.5
1      Bob    90       80     85.0
2  Charlie    78       75     76.5
3    David    60       65     62.5
"""
print(failures)
"""
    Name  Math  English  Average
3  David    60       65     62.5

如果没有的话
Empty DataFrame
Columns: [Name, Math, English, Average]
Index: []
"""
