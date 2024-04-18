# 213. 打家劫舍 II

### 与 198 不同
### 198: 无环
### 213: 有环

from typing import List

def rob_no_circle(nums):
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-2], dp[i-3])+nums[i]

        return max(dp[-2:])

class Solution:
    def rob(self, nums: List[int]) -> int:
        ### solution 2: dp + 跑2遍 :
        ### 选 nums[0]: 问题变成 无环 nums[2] - nums[n-2](左右包括)
        ### 不选 nums[0]: 变成 无环 nums[1] - nums[n-1](左右包括)
        n = len(nums)
        if n <= 3:
            return max(nums)
        
        a = nums[0] + rob_no_circle(nums[2:n-1])
        b = rob_no_circle(nums[1:])

        ans = max(a, b)
        return ans

        ### solution 1: dp + 跑两遍（把第一个数换到最后再跑一遍）
        # n = len(nums)
        # if n <= 3:
        #     return max(nums)

        # ans = -1
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # choose_0 = [True] + [False] * (n-1)

        # for i in range(2, n-1):
        #     if dp[i-2] < dp[i-3]:
        #         dp[i] = dp[i-3] + nums[i]
        #         choose_0[i] = choose_0[i-3]
        #     elif dp[i-2] > dp[i-3]:
        #         dp[i] = dp[i-2] + nums[i]
        #         choose_0[i] = choose_0[i-2]
        #     else:
        #         dp[i] = dp[i-2] + nums[i]
        #         choose_0[i] = choose_0[i-2] & choose_0[i-3]
        
        # if (not choose_0[n-3]) and (not choose_0[n-4]):
        #     dp[n-1] = max(dp[n-4], dp[n-3]) + nums[n-1]
        # elif (choose_0[n-3]) and (not choose_0[n-4]):
        #     dp[n-1] = dp[n-4] + nums[n-1]
        # elif (not choose_0[n-3]) and (choose_0[n-4]):
        #     dp[n-1] = dp[n-3] + nums[n-1]
        # else:
        #     dp[n-1] = max(dp[n-4], dp[n-3])
        
        # ans = max(dp[-3:])

        
        
        
        # new_nums = nums[1:] + [nums[0]]
        
        # dp = [0] * n
        # dp[0] = new_nums[0]
        # dp[1] = new_nums[1]
        # choose_0 = [True] + [False] * (n-1)

        # for i in range(2, n-1):
        #     if dp[i-2] < dp[i-3]:
        #         dp[i] = dp[i-3] + new_nums[i]
        #         choose_0[i] = choose_0[i-3]
        #     elif dp[i-2] > dp[i-3]:
        #         dp[i] = dp[i-2] + new_nums[i]
        #         choose_0[i] = choose_0[i-2]
        #     else:
        #         dp[i] = dp[i-2] + new_nums[i]
        #         choose_0[i] = choose_0[i-2] & choose_0[i-3]
        
        # if (not choose_0[n-3]) and (not choose_0[n-4]):
        #     dp[n-1] = max(dp[n-4], dp[n-3]) + new_nums[n-1]
        # elif (choose_0[n-3]) and (not choose_0[n-4]):
        #     dp[n-1] = dp[n-4] + new_nums[n-1]
        # elif (not choose_0[n-3]) and (choose_0[n-4]):
        #     dp[n-1] = dp[n-3] + new_nums[n-1]
        # else:
        #     dp[n-1] = max(dp[n-4], dp[n-3])
        
        # ans = max(ans, max(dp[-3:]))

        # return ans
