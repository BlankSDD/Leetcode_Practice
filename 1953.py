# 1953. 你可以工作的最大周数

from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = max(milestones)
        s = sum(milestones)

        # res = 2*m - s

        # if res > 0:
        #     ans = 2*s - 2*m + 1
        # else:
        #     ans = s

        return s - max(m - (s-m+1), 0)
