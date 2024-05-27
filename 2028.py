# 2028. 找出缺失的观测数据

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        rest = (m+n)*mean - sum(rolls)

        if (rest > 6 * n) or (rest < 1 * n):
            return []
        
        # 9/4 = 2 ...... 1   2223
        # 18/8 = 2 ...... 2  2223 2223
        # 36/16 = 2 ...... 4 2223 2223 2223 2223
        ans = [rest//n] * (n-rest%n) + [rest//n+1] * (rest%n)
        return ans
