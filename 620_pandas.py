# 620. 有趣的电影

# python 的 pandas library，专门用于处理 数据库 的 library
# https://zhuanlan.zhihu.com/p/602625087
# https://www.runoob.com/pandas/pandas-dataframe.html


import numpy as np
import pandas as pd
import random



# np.random.seed(5)#设置种子
# a=np.random.randint(1,10,(6,6))#生成随机矩阵
# col=[chr(i) for i in range(65,71)]#生成大写字母列表
# row=[chr(i) for i in range(97,103)]#生成小写字母列表
# df=pd.DataFrame(a,columns=col,index=row)
# print("df:\n",df)

# ######### 注： 下列均为： [a,b] 前包后不包 == [a,b)
# #提取行
# print("df[0:3]:\n",       df[0:3])
# #提取列
# print("df['A']:\n",       df['A']) #单列
# print("df[['A','B']]:\n", df[['A','B']]) #多列
# print("df['a','b']:\n",   df['a':'b']) #多行


# # iloc: 根据 index 来切片： [1,3] 行， [5,8] 列 
# df.iloc[ 1:3 , 5:8 ]

# # loc: 根据 label 来切片： 
# df.loc[ 'a':'b', ['A', 'B'] ]

# print(df.at['a','A'])#标签选取
# print(df.iat[0,1])#位置选取

# # 混合切片
# print("df1:\n",     df.loc[:,"A"][0:3])#先按标签提取列，在按位置提取行，同df["A"][0:3]
# print("df2:\n",     df.iloc[0]["A"])#先按位置提取行，再按标签提取列，实际为一个数，同df.iloc[0,:]["A"]
# print("df3:\n",     df.iloc[:,5]["a"])#df.iloc[:,5]提取的为一列，是Series类型可直接再按标签取,同df.iloc[:,5].lic["a"]
# print("df4:\n",     df.iloc[:,0:2].loc["a"])#先按位置，再按标签，df.iloc[:,0:2]是df

# # 按条件筛选区域
# print("df[df['A']>7]:\n",               df[df['A']>7])
# df[ (df['A'] > 10) & (df['B'] != '123456') | (df['C'].isin([1,2,3])) ]

# print("df.loc[df['B']==1,:]:\n",        df.loc[df['B']==1,:])#等同df.loc[df.loc[:,'B']==1,:]、df.loc[df.iloc[:,1]==1,:]
# print("df.loc[df.iloc[:,1]==1,:]:\n",   df.loc[df.iloc[:,1]==1, : ])
# print("df.loc[:,df.loc['a',:]==7]:\n",  df.loc[ : , df.loc['a',:]==7])


# # 排序 （实际 df 并未排序）
# df.sort_values('rating', ascending=False)





import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    
    # solution 2：两个条件 分开 切片
    # tmp = cinema.iloc[[i%2==0 for i in range(len(cinema.index))], :]
    # tmp = tmp[tmp['description'] != 'boring']

    # solution 1: 直接 两个列 的条件 切片
    tmp = cinema[ (cinema['description'] != 'boring') & (cinema['id']%2)]
    tmp = tmp.sort_values('rating', ascending=False)
    
    return tmp
