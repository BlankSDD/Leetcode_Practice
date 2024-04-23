# 39. 组合总和

# 类似的题目
# 39
# 216
# 377

import bisect
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ### solution 2: 逆向，做减法，从target向下减，直接递归
        ans = []
        for i, c in enumerate(candidates):
            if c == target:
                ans.append([c])
            elif (c < target):
                for each in self.combinationSum(candidates[i:], target-c):
                    ans.append( each + [c] )

        return ans
        
        
        ### solution 1: dfs，正向，从最小的开始做加法
        # candidates.sort()
        # ind = bisect.bisect_right(candidates, target)
        # candidates = candidates[:ind]

        # if not candidates:
        #     return []
        
        # ans = []
        # def dfs(t, input):
        #     for c in candidates:
        #         if input and (c < input[-1]):
        #             continue

        #         if t+c == target:
        #             ans.append(input+[c])
        #             return
        #         elif t+c > target:
        #             return
        #         else:
        #             dfs(t+c, input+[c])

        # dfs(0, [])
        # return ans
