# 2960. 统计已测试设备

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for each in batteryPercentages:
            if each > ans:
                ans += 1
        return ans
