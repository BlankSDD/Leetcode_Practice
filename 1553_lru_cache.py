# 1553. 吃掉 N 个橘子的最少天数

# 前几个
#    0  1  2  3  4  5  6
from functools import lru_cache


d = [0, 1, 2, 2, 3, 4, 3]

class Solution:
    ### solution 1: DFS 递归,超时了
    # def minDays(self, n: int) -> int:
    #     if (n <= 6):
    #         return d[n]
        
    #     ans = 1+self.minDays(n-1)
    #     if (not n%3):
    #         ans = min(ans, 1+self.minDays(n//3))
    #     elif (not n%2):
    #         ans = min(ans, 1+self.minDays(n//2))
        
    #     return ans


    ### solution 2: DFS + 缓存 + 记忆化搜索过的空间 + 优化除法
    # 装饰器语法, 用于使用函数来缓存函数的结果

    # @functools.lru_cache(maxsize, typed)
    # def XXXX(a):
    #     return b
    # 缓存（Cache）指的是将部分数据存储在内存中，以便下次能够更快地访问这些数据，这也是一个典型的用空间换时间的例子。一般用于缓存的内存空间是固定的，当有更多的数据需要缓存的时候，需要将已缓存的部分数据清除后再将新的缓存数据放进去。需要清除哪些数据，就涉及到了缓存置换的策略，LRU（Least Recently Used，最近最少使用）是很常见的一个

    # 关键字参数： maxsize 表示缓存容量，如果为 None 表示容量不设限， typed 表示是否区分参数类型，注释中也给出了解释，如果 typed == True，那么 f(3) 和 f(3.0) 会被认为是不同的函数调用。

    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if (n <= 6):
            return d[n]

        ans = min(n%2+self.minDays(n//2), n%3+self.minDays(n//3))
        return ans+1
