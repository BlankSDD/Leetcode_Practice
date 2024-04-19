# 2537. 统计好子数组的数目

from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ### solution 2: 1的优化，双指针, 遍历 右端点固定的时候，
        ###             左端点 向右移 的最大位置
        ans = 0
        n = len(nums)

        l = 0
        p = 0
        cnt = defaultdict(int)
        
        for x in nums:
            p += cnt[x]
            cnt[x] += 1

            while p - (cnt[nums[l]]-1) >= k:
                cnt[nums[l]] -= 1
                p -= cnt[nums[l]]
                l += 1
            
            if p >= k:
                ans += l + 1

        return ans


        ### solution 1: 暴力遍历，超时
        # ans = 0

        # n = len(nums)
        
        # min_l = int( pow(2*k, 1/2) ) - 1
        # while min_l*min_l < k:
        #     min_l += 1
        
        # if n < min_l:
        #     return 0

        # for i in range(n-min_l+1):
        #     cnt = collections.Counter(nums[i:i+min_l-1])
        #     total = 0
        #     for v in cnt.values():
        #         total += v*(v-1)//2

        #     for j in range(i+min_l-1, n):
        #         cnt[nums[j]] += 1
        #         total += cnt[nums[j]]-1

        #         if total >= k:
        #             ans += n-j
        #             break
        
        # return ans
