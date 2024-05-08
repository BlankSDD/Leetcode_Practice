# 2079. 给植物浇水

from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        cur = capacity
        ans = n
        for i in range(n):
            if cur >= plants[i]:
                cur -= plants[i]
            else:
                cur = capacity - plants[i]
                ans += 2*i
        return ans
