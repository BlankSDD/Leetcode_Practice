# 575. 分糖果

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ### solution 2: 直接处理整个 list
        return min(len(set(candyType)), len(candyType) // 2)

        ### solution 1: 遍历计数不同种类数量
        # n = len(candyType)
        # ans = 0
        # has_eaten = set()
        # for c in candyType:
        #     if not (c in has_eaten):
        #         ans += 1
        #         has_eaten.add(c)
        #     if 2*ans >= n:
        #         break

        # return ans 
