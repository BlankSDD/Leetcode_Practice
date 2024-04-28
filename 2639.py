# 2639. 查询网格图中每一列的宽度

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        ans = [ len(str(x)) for x in grid[0] ]

        for i in range(1, m):
            for j in range(n):
                ans[j] = max( ans[j], len(str(grid[i][j])) )
        
        return ans
