import pandas as pd

print(pd.Series([1,2,3]))
# 0    1
# 1    2
# 2    3
# dtype: int64  【列表 改 Series】


Series_value = [1,"apple",4.15,"dood"]
s1 = pd.Series(Series_value)
print(s1)
# 0        1
# 1    apple
# 2     4.15
# 3     dood
# dtype: object 【列表 改 Series】


index_name = ["a","b","c","d"]
s2 = pd.Series(Series_value,index=index_name)
print(s2)
# a        1
# b    apple
# c     4.15
# d     dood
# dtype: object  【赋与 索引名】


df_value = {
    "animal":["dog","cat","bear"],
    "owner":["alice","bob","cathy"],
    "age":[15,18,19]}
index_name = ['a','b','c']
df1=pd.DataFrame(df_value)
print(df1)
#   animal  owner  age
# 0    dog  alice   15
# 1    cat    bob   18
# 2   bear  cathy   19

df2=pd.DataFrame(df_value,index=index_name)
print(df2)
#   animal  owner  age
# a    dog  alice   15
# b    cat    bob   18
# c   bear  cathy   19


for i in range(5):
    print(i, end=' ')  #end=' '，在每次输出数字之后没有换行，而是用空格进行分隔
#0 1 2 3 4 0

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4









