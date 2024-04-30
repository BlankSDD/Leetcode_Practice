# 2798. 满足目标工作时长的员工数目

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for h in hours:
            if h >= target:
                ans += 1

        return ans
