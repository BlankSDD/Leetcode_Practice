# 2105. 给植物浇水 II

from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        
        a = 0
        acur = capacityA
        
        b = n-1
        bcur = capacityB

        ans = 0

        while a < b:
            if acur < plants[a]:
                acur = capacityA
                ans += 1
            acur -= plants[a]
            a += 1

            if bcur < plants[b]:
                bcur = capacityB
                ans += 1
            bcur -= plants[b]
            b -= 1
        
        if (a == b) and (max(acur, bcur) < plants[a]):
            ans += 1
        
        return ans
            
