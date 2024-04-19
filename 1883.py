# 1883. 准时抵达会议现场的最小跳过休息次数

from math import inf
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

        ### dp 动态规划 
        ### dp[i][j] 的值 为 经过 第 0 至 (i-1) 段路后 (一共已经经过了 i 段路)，在 第 i 个路面前，在此前跳过了 j 次， 最短的时间
        ### 此时，要考虑 最后一段路 (i-1) 是否要跳过
        ### 如果 没有跳过： f[i][j] = f[i-1][j] + (i-1)经过时间 + (i-1)等待时间
        ### 如果 跳过： f[i][j] = f[i-1][j-1] + (i-1)经过时间
        ### 由于要尽可能小， 则取 两种情况 的最小值

        # 浮点数的除法会产生的误差
        # 可以改用 乘法， 把所有的 dist 和 houseBefore 乘上 speed
        # 则： 此时，休息等待时间 会变成 下一个 speed 的整数倍才能继续移动
        
        ### solution 1: 除法，要注意 误差
        # if sum(dist) > (speed * hoursBefore):
        #     return -1
        # if len(dist) == 1:
        #     return 0

        # # 浮点数的除法会产生的误差
        # EPS = 1e-7

        # n = len(dist)

        # dp = [ [inf] * (n+1) for i in range(n+1)  ]
        # dp[0][0] = 0.0

        # for i in range(1, n+1):
            
        #     # 一共经过 i 段路，最多跳 i 次
        #     for j in range(i+1):
        #         # 最后一次 不跳
        #         if j != i:
        #             # 除法要减去误差
        #             not_jump = math.ceil(dp[i-1][j] + dist[i-1] / speed - EPS)
        #         # 最后一次 不跳，不可能达到 i 次跳跃
        #         else:
        #             not_jump = inf

        #         # 最后一次 跳
        #         # 最后一次 跳，不可能达到 0 次跳跃
        #         if not j:
        #             jump = inf
        #         else:
        #             jump = dp[i-1][j-1] + dist[i-1] / speed
                
        #         dp[i][j] = min(jump, not_jump)

        # for j in range(n+1):
        #     if (dp[n][j] <= hoursBefore + EPS):
        #         return j
        
        # return -1

        ### solution 2: 乘法法，要注意 等待时间变化
        # if sum(dist) > (speed * hoursBefore):
        #     return -1
        # if len(dist) == 1:
        #     return 0

        # n = len(dist)

        # dp = [ [inf] * (n+1) for i in range(n+1)  ]
        # dp[0][0] = 0

        # for i in range(1, n+1):
            
        #     # 一共经过 i 段路，最多跳 i 次
        #     for j in range(i+1):
        #         # 最后一次 不跳
        #         if j != i:
        #             # 除法要减去误差
        #             not_jump = dp[i-1][j] + dist[i-1]
        #             if not_jump % speed:
        #                 not_jump += speed - (not_jump % speed)


        #         # 最后一次 不跳，不可能达到 i 次跳跃
        #         else:
        #             not_jump = inf

        #         # 最后一次 跳
        #         # 最后一次 跳，不可能达到 0 次跳跃
        #         if not j:
        #             jump = inf
        #         else:
        #             jump = dp[i-1][j-1] + dist[i-1]
                
        #         dp[i][j] = min(jump, not_jump)

        # for j in range(n+1):
        #     if (dp[n][j] <= hoursBefore * speed):
        #         return j
        
        # return -1

        ### solution 3: 优化 dp 仅存储上一次的 dp
        if sum(dist) > (speed * hoursBefore):
            return -1
        if len(dist) == 1:
            return 0

        n = len(dist)

        dp = [inf] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            new_dp = [inf] * (n+1)
            # 一共经过 i 段路，最多跳 i 次
            for j in range(i+1):
                # 最后一次 不跳
                if j != i:
                    # 除法要减去误差
                    not_jump = dp[j] + dist[i-1]
                    if not_jump % speed:
                        not_jump += speed - (not_jump % speed)


                # 最后一次 不跳，不可能达到 i 次跳跃
                else:
                    not_jump = inf

                # 最后一次 跳
                # 最后一次 跳，不可能达到 0 次跳跃
                if not j:
                    jump = inf
                else:
                    jump = dp[j-1] + dist[i-1]
                
                new_dp[j] = min(jump, not_jump)
            
            dp = new_dp

        for j in range(n+1):
            t = dp[j]
            if (t <= hoursBefore * speed):
                return j
        
        return -1

        


        

