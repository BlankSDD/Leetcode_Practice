# 2965. 找出缺失和重复的数字

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ### solution 2: 先建一个表 记录
        n = len(grid)
        a = -1
        b = -1
        tmp = [False] * (n*n+1)

        for i in range(n):
            for j in range(n):
                cur = grid[i][j]

                if tmp[cur]:
                    a = cur
                
                tmp[grid[i][j]] = True
        
        for j in range(1, n*n+1):
            if not tmp[j]:
                b = j
                break
        
        return [a,b]


        ### solution 1: 在原表上更改，最小化空间
        # n = len(grid)
        # a = -1
        # b = -1

        # for i in range(n):
        #     for j in range(n):

        #         cur = grid[i][j]%(n*n) - 1
        #         if grid[cur//n][cur%n] > n*n:
        #             a = cur+1

        #         grid[cur//n][cur%n] += n*n

        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] <= n*n:
        #             b = n*i + j + 1
        #             break
        
        # if a == 0:
        #     a += n*n
        # return [a, b]
