# 741. 摘樱桃

# 741. 摘樱桃       AB 均从左上到右下
# 1463. 摘樱桃 II   A 左上往下， B 右上往下

from math import inf
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ### solution 2: 可以优化 solution 1 中的 dp， 只保留上一步的状态
        ###             但是要注意，因为是 AB 走，所以会影响本次状态转移

        ### solution 1: 等价转换成，有两个人从 (0,0) 出发，向下或向右走到 (N−1,N−1) 时，摘到的樱桃个数之和的最大值，两个人记为 A B
        ### dp[k][x1][x2]
        ### 每个人走的总步数 k (无论向右/下,总步数相同)
        ### A 向下走 x1 步，则向右走 k-x1 步
        ### B 向下走 x2 步，则向右走 k-x2 步
        ### dp的状态转移，4种情况
        ### 1. AB 都向右走
        ### 2. A 向下 B 向右
        ### 3. A 向右 B 向下
        ### 4. AB 都向下走

        n = len(grid)
        dp = [ [ [-inf]*n for _ in range(n) ] for _ in range(2*n-1) ]
        
        dp[0][0][0] = grid[0][0]
        
        for k in range(1, 2*n-1):

            # A 向下走 x1 步，向下 最少 0 步，最多 n-1 步
            #   向右走 k-x1 步，最少 0 步，最多 n-1 步
            #   0 <= x1 <= n-1
            #   0 <= k-x1 <= n-1  ----->  k-n+1 <= x1 <= k
            #   得到 x1 的范围： max(k-n+1, 0) <= x1 <= min(k, n-1)
            for x1 in range(max(k-n+1, 0), min(k+1, n)):
                y1 = k-x1

                # 有荆棘，过不去，跳过
                if grid[x1][y1] == -1:
                    continue
                
                for x2 in range(max(k-n+1, 0), min(k+1, n)):
                    y2 = k-x2

                    if grid[x2][y2] == -1:
                        continue
                    
                    # 情况1：AB 都向右
                    tmp = dp[k-1][x1][x2]

                    # 情况2：A 向下 B 向右
                    if x1:
                        tmp = max(tmp, dp[k-1][x1-1][x2])
                    
                    # 情况3：A 向右 B 向下
                    if x2:
                        tmp = max(tmp, dp[k-1][x1][x2-1])
                    
                    # 情况4：AB 都向下
                    if x1 and x2:
                        tmp = max(tmp, dp[k-1][x1-1][x2-1])
                    
                    # 避免 AB 在同一个位置重复摘取樱桃
                    if x1 == x2:
                        tmp += grid[x1][y1]
                    else:
                        tmp += (grid[x1][y1] + grid[x2][y2])
                    
                    dp[k][x1][x2] = tmp
        
        return max(dp[-1][-1][-1], 0)
                
