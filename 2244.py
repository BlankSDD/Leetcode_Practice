# 2244. 完成所有任务需要的最少轮数

import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        cnt = collections.Counter(tasks)
        
        if (1 in cnt.values()):
            return -1
        
        for v in cnt.values():
            ans += v//3

            # 除 3 余 1， 则 2+2
            # 除 3 余 2， 则 3+2
            # 一定会多一次
            if v%3:
                ans += 1
        
        return ans
            
            
