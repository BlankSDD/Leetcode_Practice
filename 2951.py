# 2951. 找出峰值
from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        if n <= 2:
            return []

        ans = []

        pre = mountain[0]
        cur = mountain[1]
        nxt = int
        for i in range(2,n):
            nxt = mountain[i]
            if cur > pre and cur > nxt:
                ans.append(i-1)
            
            pre = cur
            cur = nxt
        
        return ans
