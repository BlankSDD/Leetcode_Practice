# 1235. 规划兼职工作

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ### solution 1: 打包 + 根据结束时间排序 + dp
        ### dp[i] 即 第 i-1 个兼职做不做
        ### 状态转移情况： 1. 不做 dp[i-1]
        ###               2. 做， 则需要在 第 i-1 个兼职开始前找到最后一个兼职
        ### 怎么找到 第 i-1 个兼职开始前找到最后一个兼职：
        ### 二分法： i-1 的开始时间，插入到结束时间的右侧 k
        ###         dp[k] 即 k-1 个兼职
        n = len(startTime)
        s_e_p = sorted( zip(startTime, endTime, profit), key=lambda x:x[1]  )

        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            k = bisect.bisect_right(s_e_p, s_e_p[i-1][0], key=lambda x:x[1])
            dp[i] = max(dp[i-1], dp[k]+s_e_p[i-1][2])

        return dp[-1]

        
        return 0
