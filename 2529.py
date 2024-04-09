# 2529. 正整数和负整数的最大计数
import bisect


class Solution:
    def maximumCount(self, nums):
        ### solution 1: 二分查找 0 插入的位置
        n = len(nums)
        neg = bisect.bisect_left(nums, 0)
        pos = 0
        for i in range(neg, n):
            if nums[i] > 0:
                pos = n - i
                break
        return max(neg, pos)
