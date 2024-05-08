# 2462. 雇佣 K 位工人的总代价

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ### solution 2: 两个heap
        n = len(costs)

        if (k + 2 * candidates) > n:
            heapq.heapify([costs])
            return sum(heapq.nsmallest(k, costs))

        l = candidates-1
        r = n-candidates

        lhp = costs[:candidates]
        heapq.heapify(lhp)

        rhp = costs[n-candidates:]
        heapq.heapify(rhp)

        lm = heapq.heappop(lhp)
        rm = heapq.heappop(rhp)

        ans = 0
        for i in range(k):
            
            if lm <= rm:
                ans += lm
                l += 1
                lm = heapq.heappushpop(lhp, costs[l])
                # heapq.heappush(lhp, costs[l])
                # lm = heapq.heappop(lhp)
            else:
                ans += rm
                r -= 1
                heapq.heappush(rhp, costs[r])
                rm = heapq.heappop(rhp)
        
        return ans


        ### solution 1: 一个 heap
        # n = len(costs)

        # if (k + 2 * candidates) > n:
        #     heapq.heapify([costs])
        #     return sum(heapq.nsmallest(k, costs))

        # l = candidates-1
        # r = n-candidates

        # hp = []

        # for i in range(candidates):
        #     heapq.heappush(hp, (costs[i], i))
        #     heapq.heappush(hp, (costs[-i-1], n-i))

        # ans = 0
        # for i in range(k):
        #     c, index = heapq.heappop(hp)
        #     ans += c

        #     if index <= l:
        #         l += 1
        #         heapq.heappush(hp, (costs[l], l))
                
        #     else:
        #         r -= 1
        #         heapq.heappush(hp, (costs[r], r))
        
        # return ans
