# 1052. 爱生气的书店老板

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        ### solution 1: 维护一个滑动窗口
        n = len(customers)
        if minutes >= n:
            return sum(customers)

        not_sat = 0
        total_sat = 0
        for i in range(minutes):
            if grumpy[i]:
                not_sat += customers[i]
            else:
                total_sat += customers[i]

        max_not_sat = not_sat

        for i in range(minutes, n):
            if grumpy[i-minutes]:
                not_sat -= customers[i-minutes]

            if grumpy[i]:
                not_sat += customers[i]
            else:
                total_sat += customers[i]
            
            max_not_sat = max(max_not_sat, not_sat)
        
        return total_sat + max_not_sat

                
