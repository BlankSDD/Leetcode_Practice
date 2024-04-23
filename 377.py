# 377. 组合总和 Ⅳ

# 类似的题目
# 39
# 216
# 377

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ### solurion 2: dp
        ans = 0
        
        dp = [1] + [0] * (target)

        for i in range(min(nums), target+1):
            for j in nums:
                if (j <= i) and (dp[i-j]):
                    dp[i] += dp[i-j]

        return dp[-1]

        ### solution 1: dfs， 超时
        # nums.sort()
        
        # ans = 0
        # def dfs(t):
        #     for i in nums:
        #         if (t < i):
        #             return 
        #         elif (i == t):
        #             nonlocal ans
        #             ans += 1
        #             return
        #         else:
        #             dfs(t-i)
        
        # dfs(target)
        # return ans
                
