# 857. 雇佣 K 名工人的最低成本

import heapq
from math import inf
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        ### solutuion 1: 工资排序 + 做事量大根堆 + 贪心遍历
        ### w/q 即为 相同的事，给钱多少
        ### 根据 w/q 排序后： 0.1， 0.2
        ### 排序后，后面一个人，无法接受前面一个人的价格，所以单价都为最后一人
        ###
        ### 但是，算总价格，与 做的 量 有关， 量 也得排序
        ### 维持一个 k 个人的队列，始终以最后一个人的价格为单价
        ### 但是新加一个人，价格就要变，但是 做的 量 要踢出做最多的人
        n = len(quality)
        qw = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        
        hp = [ -q for q,w in qw[:k-1] ]
        totalq = - sum( hp )

        heapq.heapify(hp)

        ans = inf
        
        for q,w in qw[k-1:]:
            totalq += q
            heapq.heappush(hp, -q)

            # 最后一个人的单价 * 总工作量
            ans = min(ans, w/q*totalq)
            # 所有人价格一样，把做最多的事的人踢出去（给钱最多）
            totalq += heapq.heappop(hp)
        
        return ans
