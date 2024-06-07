# 3038. 相同分数的最大操作数目 I

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return 0

        score = nums[0] + nums[1]
        for i in range(1, n//2):
            if (nums[2*i] + nums[2*i+1] != score):
                return i
        
        return n//2
            
