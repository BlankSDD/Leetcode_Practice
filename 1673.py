# 1673. 找出最具竞争力的子序列

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        ### solution 1: 遍历+堆栈
        ###             1. 创建 ans， 遍历 nums
        ###             2. while ans不空 且 当前小于ans[-1] 且 剩下数量足够形成 k 长度， 则 让 ans 一直 pop直到空（说明当前为最小元素，可以放在最前面，此时 ans 中只剩下最小元素升序排列）（即: 在长度允许的情况下，在上一个最小元素之后，找到下一个最小元素（大于上一个，如果下一个更小，则替换上一个））
        ###             3. 如果长度不够 k， 加入当前元素
        n = len(nums)
        ans = []
        for i in range(n):
            while ans and (ans[-1] > nums[i]) and (len(ans) + n-i > k):
                ans.pop()
            
            if (len(ans) < k):
                ans.append(nums[i])

        return ans
