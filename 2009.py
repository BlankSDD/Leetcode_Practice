# 2009. 使数组连续的最少操作数
import bisect

class Solution:
    def minOperations(self, nums):
        ### solution 2: 去重 + 双指针 + 优化
        n1 = len(nums)
        new_nums = sorted((set(nums)))
        n2 = len(new_nums)

        i = 0
        j = bisect.bisect_right(new_nums, new_nums[i]+n1-1)
        max_nr = j-i

        for i in range(1, n2):

            r = new_nums[i]+n1-1
            while (j <= n2-1) and new_nums[j] <= r:
                j += 1
            
            max_nr = max(max_nr, j-i)
            if j == n2:
                break
        return n1-max_nr
        
        ### solution 1: 单指针遍历，超时
        # n = len(nums)
        # nums.sort()
        # ans = inf
        # for i in range(n):
        #     j = bisect.bisect_right(nums, nums[i]+n-1)
        #     ans = min(ans, n-len(set(nums[i:j])))
        #     if j == n:
        #         break
        # return ans



        

