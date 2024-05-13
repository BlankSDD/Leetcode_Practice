# 994. 腐烂的橘子

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ### solution 1: BFS + 计数 好的数量 比较 新坏的数量
        m = len(grid)
        n = len(grid[0])

        good = 0
        new_bad = 0

        cur = []
        nxt = []

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    good += 1
                elif (grid[i][j] == 2):
                    cur.append([i,j])
        
        if (not good):
            return 0


        t = -1
        while cur:
            for i,j in cur:
                for nxt_i,nxt_j in [[i-1,j], [i,j-1], [i,j+1], [i+1,j]]:
                    if (0 <= nxt_i <= m-1) and (0 <= nxt_j <= n-1) and (grid[nxt_i][nxt_j] == 1):
                        grid[nxt_i][nxt_j] = 2
                        new_bad += 1
                        nxt.append( [nxt_i,nxt_j] )
            
            cur = nxt
            nxt = []
            t += 1
        
        if (good == new_bad):
            return t
        else:
            return -1
        
        # 如果不计数，可以判断是否有 1
        # sum() 也可以用于列表的展开，效果相当于各子列表相加
        # lst = [[1, 2], [3, 4]]
        # print(sum(lst, [])) 
        # #[1, 2, 3, 4]
        ## 如下所示:

        # if 1 in sum(grid, []):
        #     return -1
        # else:
        #     return t
