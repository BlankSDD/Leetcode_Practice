# 1463. 摘樱桃 II

# 741. 摘樱桃       AB 均从左上到右下，确定了 起/终点
# 1463. 摘樱桃 II   A 左上往下， B 右上往下，没有确定 终点

from math import inf
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ### solution 2: 可以优化 solution 1 中的 dp， 只保留上一层的状态
        
        ### solution 1: 两个人记为 A B
        ### dp[k][x1][x2]
        ### 每个人向下走的层数，总层数相同，都向下走了 k 层
        ### A 的横坐标为 x1
        ### B 的横坐标为 x2
        ### dp的状态转移，9种情况
        ### 上一层 A 左上/正上/右上  *  上一层 B 左上/正上/右上
        ### dp[k-1][x1][x2]   ----->    dp[k][x1][x2]
        ### 

        n = len(grid)
        m = len(grid[0])

        # 初始化为 -inf
        # 如果为 0， 不好判断 上一层中 数量为 0 的情况 + 初始为 0 的情况
        #           且，此时 A B 可以从中间开始向下走
        #           例如： [0, 1, 1, 2, 1, 0]
        #                  [1, 1, 7, 8, 1, 2]
        #           此时， dp[0] 第0层全为 0
        #           计算   dp[1] 第1层就会遍历到 7, 8 计算从中间开始的 向下走
        dp = [ [[-inf]*m for _ in range(m) ] for _ in range(n) ]
        
        dp[0][0][m-1] = grid[0][0] + grid[0][m-1]

        for i in range(1, n):
            
            # A 每次最多向右走 1 格
            for x1 in range( min(i+1, m) ):

                # B 每次最多向左走 1 格
                for x2 in range( max(m-i-1, 0), m ):
                    
                    # AB 均向上
                    tmp = dp[i-1][x1][x2]
                    
                    # A 左
                    if x1:
                        # B 左
                        if x2:
                            tmp = max(tmp, dp[i-1][x1-1][x2-1])
                        # B 中
                        tmp = max(tmp, dp[i-1][x1-1][x2])
                        # B 右
                        if x2 < m-1:
                            tmp = max(tmp, dp[i-1][x1-1][x2+1])
                    
                    # A 中
                    # B 左
                    if x2:
                        tmp = max(tmp, dp[i-1][x1][x2-1])
                    # B 右
                    if x2 < m-1:
                        tmp = max(tmp, dp[i-1][x1][x2+1])
                    
                    # A 右
                    if x1 < m-1:
                        # B 左
                        if x2:
                            tmp = max(tmp, dp[i-1][x1+1][x2-1])
                        # B 中
                        tmp = max(tmp, dp[i-1][x1+1][x2])
                        # B 右
                        if x2 < m-1:
                            tmp = max(tmp, dp[i-1][x1+1][x2+1])
                    
                    # 走到同一格，只算一次
                    if x1 == x2:
                        dp[i][x1][x2] = tmp + grid[i][x1]
                    else:
                        dp[i][x1][x2] = tmp + grid[i][x1] + grid[i][x2]
        
        # 最后一层中的最大值
        return max( [ max(each) for each in dp[n-1] ] )
