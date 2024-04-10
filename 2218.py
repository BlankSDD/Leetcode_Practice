# 2218. 从栈中取出 K 个硬币的最大面值和

class Solution:
    def maxValueOfCoins(self, piles, k):
        ### solution 1: 背包问题 -- 前缀和 + dp
        n = len(piles)

        # 前缀和
        pre = []
        for pile in piles:
            tmp = [0]
            for p in pile:
                tmp.append(tmp[-1] + p)
            pre.append(tmp)
        
        # dp:  从前 n 个栈中， 取 k 个硬币的最大结果
        # n 行， k 列
        dp = [ [0]*(k+1) for i in range(n) ]

        # 初始化第 1 个栈 取硬币的情况
        for j in range( min(k+1, len(piles[0])+1) ):
            dp[0][j] = pre[0][j]

        # 从前 2 个栈 开始
        # 即：前 i 个栈 取硬币
        for i in range(1, n):
            ni = len(piles[i])

            # 从前 i 个栈中 遍历 取 x 个硬币的结果
            for x in range(1, k+1):

                # 第 i 个栈 取 j 个硬币的结果
                # 则: 前 i-1 个栈 取 x-j 个硬币
                for j in range(min(k+1, ni+1)):
                    if x < j:
                        break
                    cur_add = pre[i][j]
                    dp[i][x] = max( dp[i][x], dp[i-1][x-j] + cur_add )
        
        return dp[n-1][k]
